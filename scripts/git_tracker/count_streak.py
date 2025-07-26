import subprocess
from datetime import datetime, timedelta
import json
import os

LOG_FILE = "scripts/git_tracker/commit_log.json"

def get_commit_dates():
    result = subprocess.run(["git", "log", "--pretty=format:%cd", "--date=short"], 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text = True
                            )
    if result.returncode != 0:
        print("Error getting git log:", result.stderr)
        return []
    dates = result.stdout.strip().split('\n')
    return list(sorted(set(dates), reverse = True))

def count_streak(dates):
    today = datetime.today().date()
    streak = 0
    for date_str in dates:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if date == today - timedelta(days = streak):
            streak += 1
        else:
            break
    return streak

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return set(json.load(f))
    else:
        return set()

def save_log(dates):
    with open(LOG_FILE, "w") as f:
        json.dump(sorted(dates), f, indent = 2)

def update_log(commit_dates):
    log = load_log()
    log.update(commit_dates)
    save_log(list(log))

if __name__ == "__main__":
    commit_dates = get_commit_dates()
    update_log(commit_dates)
    log = load_log()
    sorted_log = sorted(log, reverse=True)
    print(f"Your current commit streak is: {count_streak(sorted_log)} day(s)")


    