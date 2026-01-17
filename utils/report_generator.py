from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os

def generate_pdf(student_id, plan, feedback):
    filename = f"reports/{student_id}_report.pdf"
    os.makedirs("reports", exist_ok=True)

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    content = [
        Paragraph(f"Student Report: {student_id}", styles["Heading1"]),
        Paragraph(f"Learner Level: {plan['level']}", styles["Normal"]),
        Paragraph(f"Student Message: {plan['student_message']}", styles["Normal"]),
        Paragraph(f"Teacher Insight: {plan['teacher_insight']}", styles["Normal"]),
        Paragraph(f"Next Step: {plan['next_step']}", styles["Normal"]),
        Paragraph(f"Focus Area: {plan['focus_area']}", styles["Normal"]),
        Paragraph(f"AI Feedback: {feedback}", styles["Normal"]),
    ]

    doc.build(content)
    return filename
