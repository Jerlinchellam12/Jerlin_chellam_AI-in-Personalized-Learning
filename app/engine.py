import pandas as pd
import joblib

model = joblib.load("models/performance_classifier.pkl")

def classify_learner(accuracy, time, hesitation, engagement, hint):
    row = pd.DataFrame([[
        accuracy, time, hesitation, engagement, hint
    ]], columns=[
        "accuracy",
        "avg_response_time",
        "hesitation_rate",
        "engagement_score",
        "hint_usage"
    ])

    return model.predict(row)[0]