def generate_feedback(level, accuracy, hint):
    if level == "Needs Support":
        return "You should revisit the basics and take your time with examples."
    elif level == "Developing":
        return "You are improving. Focus on reducing mistakes and practice daily."
    elif level == "Competent":
        return "You understand the topic well. Try increasing speed and confidence."
    elif level == "Dependent Advanced":
        return "Try solving questions without hints to build independence."
    elif level == "Independent Mastery":
        return "Excellent work! Try advanced real-world problems."
    else:
        return "Keep learning consistently."
