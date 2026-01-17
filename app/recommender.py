import json

with open("data/content_bank.json") as f:
    content = json.load(f)

def recommend(topic, learner_type):
    return content[topic][learner_type]
