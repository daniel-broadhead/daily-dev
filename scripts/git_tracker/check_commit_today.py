import subprocess
from datetime import datetime

def committed_today():
    result = subprocess.run(["git", "log", "--pretty=format:%cd","--date=short"], capture_output=True, text = True)
    if result.returncode != 0:
        print("Failed to run git log.")
        return False
    commit_dates = result.stdout.splitlines()
    today = datetime.now().strftime("%Y-%m-&d")

    return today in commit_dates
def main():
    if committed_today():
        print("✅ You have committed today!")
    else:
        print("❌ No commit yet today. Go make one!")
if __name__ == "__main__":
    main()

