import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from joblib import dump

df = pd.read_csv("data/simulated_learners.csv")

X = df[["accuracy","avg_response_time","hesitation_rate","engagement_score","hint_usage"]]
y = df["learner_type"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train,y_train)

print(classification_report(y_test, model.predict(X_test)))

dump(model,"models/performance_classifier.pkl")
print("Model saved: models/performance_classifier.pkl")
