import pandas as pd
import numpy as np

np.random.seed(42)

n = 500
data = {
    "student_id": range(1, n+1),
    "accuracy": np.random.uniform(0.2, 1.0, n),
    "avg_response_time": np.random.uniform(2, 20, n),
    "hesitation_rate": np.random.uniform(0, 1, n),
    "engagement_score": np.random.uniform(0.2, 1.0, n),
    "hint_usage": np.random.uniform(0.0, 1.0, n)
}

df = pd.DataFrame(data)

def label(row):
    if row.accuracy < 0.45 or row.hint_usage > 0.7:
        return "Needs Support"
    elif row.accuracy < 0.65:
        return "Developing"
    elif row.accuracy < 0.8:
        return "Competent"
    elif row.hint_usage > 0.4:
        return "Dependent Advanced"
    else:
        return "Independent Mastery"

df["learner_type"] = df.apply(label, axis=1)

df.to_csv("data/simulated_learners.csv", index=False)
print("Dataset saved: data/simulated_learners.csv")
