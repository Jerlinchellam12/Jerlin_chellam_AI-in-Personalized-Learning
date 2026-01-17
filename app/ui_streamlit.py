import sys
import os

# Fix import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd

from app.engine import classify_learner
from app.recommender import recommend
from utils.logger import log_progress
from app.feedback_generator import generate_feedback
from utils.report_generator import generate_pdf


# ------------------ CONFIG ------------------
st.set_page_config(page_title="AI Personalized Learning", layout="wide")

# ------------------ SIDEBAR NAV ------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Student View", "Teacher Dashboard"])


# ======================================================
# ====================== STUDENT VIEW ==================
# ======================================================
if page == "Student View":

    st.title("🎓 AI-Powered Adaptive Learning System")

    student_id = st.text_input("Student Name/ID")
    topic = st.selectbox("Select Topic", ["fractions"])

    st.subheader("📊 Performance Input")
    accuracy = st.slider("Accuracy", 0.0, 1.0, 0.6)
    time = st.slider("Avg Response Time (sec)", 2.0, 20.0, 8.0)
    hesitation = st.slider("Hesitation Rate", 0.0, 1.0, 0.2)
    engagement = st.slider("Engagement Score", 0.0, 1.0, 0.7)
    hint = st.slider("Hint Usage Rate", 0.0, 1.0, 0.3)

    if st.button("Analyze & Adapt"):

        if not student_id.strip():
            st.error("Please enter Student Name/ID")
            st.stop()

        learner_type = classify_learner(
            accuracy, time, hesitation, engagement, hint
        )
        plan = recommend(topic, learner_type)

        # ----------- REPORT UI -----------
        st.subheader("📘 Student Learning Report")

        st.markdown(f"### 🧠 Learner Level: **{plan['level']}**")
        st.info(f"👩‍🎓 Student View: {plan['student_message']}")

        st.markdown("### ⏭ Next Step")
        st.write(plan["next_step"])

        st.markdown("### 📚 Focus Area")
        st.write(plan["focus_area"])

        st.markdown("### 🧭 Instruction Strategy")
        st.write(plan["instruction_strategy"])

        st.markdown("### 📝 Recommended Assessment")
        st.write(plan["assessment"])

        st.markdown("### 👨‍🏫 Teacher Insight")
        st.write(plan["teacher_insight"])

        st.markdown("### ⚠ Risk Indicator")
        st.write(plan["risk_flag"])

        st.markdown("### 📂 Learning Resources")
        for r in plan["resources"]:
            st.write(f"• {r}")

        # ----------- AI FEEDBACK -----------
        feedback = generate_feedback(learner_type, accuracy, hint)
        st.session_state.plan = plan
        st.session_state.feedback = feedback


        st.markdown("### 🤖 AI Feedback")
        st.success(feedback)

        # ----------- SAVE PROGRESS -----------
        log_progress(
            student_id,
            accuracy,
            time,
            hesitation,
            engagement,
            hint,
            learner_type
        )

     # ----------- PDF REPORT (FINAL FIXED VERSION) -----------

    if "pdf_bytes" not in st.session_state:
        st.session_state.pdf_bytes = None

    if "pdf_name" not in st.session_state:
        st.session_state.pdf_name = None


    if st.button("📄 Generate PDF Report"):

        if "plan" not in st.session_state or "feedback" not in st.session_state:
            st.error("Please click 'Analyze & Adapt' first.")
        else:
            try:
                plan = st.session_state.plan
                feedback = st.session_state.feedback

                path = generate_pdf(student_id, plan, feedback)

                st.write(f"PDF generated at: {path}")

                with open(path, "rb") as f:
                    pdf_bytes = f.read()

                st.session_state.pdf_bytes = pdf_bytes
                st.session_state.pdf_name = f"{student_id}_report.pdf"

                st.success("Report generated successfully! Ready for download.")

            except Exception as e:
                st.error(f"PDF generation failed: {e}")


    if st.session_state.pdf_bytes is not None:
        st.download_button(
            label="⬇ Download Student Report",
            data=st.session_state.pdf_bytes,
            file_name=st.session_state.pdf_name,
            mime="application/pdf"
        )



# ======================================================
# ==================== TEACHER DASHBOARD ===============
# ======================================================
elif page == "Teacher Dashboard":

    st.title("📊 Dashboard")

    if not os.path.exists("data/progress_log.csv"):
        st.warning("No student data available yet.")
        st.stop()

    df = pd.read_csv("data/progress_log.csv")

    if df.empty:
        st.warning("Progress file exists but contains no records.")
        st.stop()

    # Convert timestamp and sort
    # Handle timestamp safely
    if "timestamp" not in df.columns:
        df["timestamp"] = range(len(df))  # fallback index if old logs exist
    else:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    df = df.sort_values("timestamp")

    # Force numeric types (very important!)
    for col in ["accuracy", "engagement", "hint"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    selected_student = st.selectbox(
        "Select Student ID",
        df["student_id"].unique()
    )

    student_df = df[df["student_id"] == selected_student]

    st.subheader("📈 Accuracy & Engagement Over Time")
    st.line_chart(
        student_df.set_index("timestamp")[["accuracy", "engagement"]]
    )

    st.subheader("📉 Hint Usage Over Time")
    st.line_chart(
        student_df.set_index("timestamp")[["hint"]]
    )

    st.subheader("📋 Recent Activity")
    st.dataframe(student_df.tail(10), use_container_width=True)
