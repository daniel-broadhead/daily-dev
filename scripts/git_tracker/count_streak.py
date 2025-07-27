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

def calculate_longest_streak(dates):
    sorted_dates = sorted(set(datetime.strptime(d, "%Y-%m-%d").date() for d in dates))
    if not sorted_dates:
        return 0
    max_streak = current_streak = 1
    for i in range(1, len(sorted_dates)):
        if sorted_dates[i] == sorted_dates[i-1] + timedelta(days = 1):
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak


def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
            return set(data.get("dates", [])), data.get("longest_streak", 0)
    else:
        return set(), 0

def save_log(dates, longest_streak):
    with open(LOG_FILE, "w") as f:
        json.dump({
            "dates": sorted(dates),
            "longest_streak": longest_streak
        }, f, indent=2)

def update_log(commit_dates):
    log_dates, longest_streak = load_log()
    log_dates.update(commit_dates)
    new_longest_streak = max(longest_streak, calculate_longest_streak(log_dates))
    save_log(log_dates, new_longest_streak)
    return log_dates, new_longest_streak

if __name__ == "__main__":
    commit_dates = get_commit_dates()
    log_dates, longest_streak = update_log(commit_dates)
    sorted_log = sorted(log_dates, reverse=True)
    current_streak = count_streak(sorted_log)
    print(f"Your current commit streak is: {current_streak} day(s)")
    print(f"Your longest streak is {longest_streak} day(s)")
    


    