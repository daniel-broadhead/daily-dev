import subprocess
from datetime import datetime, timedelta

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

def count_streak():
    dates = get_commit_dates()
    today = datetime.today().date()
    streak = 0
    for i in range(len(dates)):
        date = datetime.strptime(dates[i], "%Y-%m-%d").date()
        if date == today - timedelta(days = streak):
            streak += 1
        else:
            break
    return streak

if __name__ == "__main__":
    print(f"Your current commit streak is: {count_streak()} day(s)")


    