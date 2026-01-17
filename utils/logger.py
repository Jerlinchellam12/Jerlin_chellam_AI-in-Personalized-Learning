import csv
from datetime import datetime
import os

LOG_FILE = "data/progress_log.csv"

def log_progress(student_id, accuracy, time, hesitation, engagement, hint, level):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "student_id",
                "accuracy",
                "time",
                "hesitation",
                "engagement",
                "hint",
                "level",
                "timestamp"
            ])

        writer.writerow([
            student_id,
            accuracy,
            time,
            hesitation,
            engagement,
            hint,
            level,
            datetime.now().isoformat()
        ])
