"""
push_to_github.py — Push all capstone changes to GitHub

Usage (terminal):
    python push_to_github.py
    python push_to_github.py "Week 9 submissions added"

Usage (inside Jupyter notebook cell):
    import subprocess
    subprocess.run(["python", "push_to_github.py", "Week 9 notebook added"], check=True)

First-time setup:
    Set your GitHub Personal Access Token as an environment variable:
        export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
    Or paste it directly in the GITHUB_TOKEN line below (not recommended for shared repos).
"""

import subprocess, sys, os
from datetime import datetime

REPO_DIR   = os.path.dirname(os.path.abspath(__file__))
GIT_USER   = "divyabhanusri24"
GIT_EMAIL  = "divyabhanusri24@gmail.com"
REMOTE_URL = "https://github.com/divyabhanusri24/imperial-aiml-capstone.git"

def run(cmd, cwd=REPO_DIR):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()

def push(commit_msg=None):
    os.chdir(REPO_DIR)

    # Git identity
    run(["git", "config", "user.name",  GIT_USER])
    run(["git", "config", "user.email", GIT_EMAIL])

    # Auth via token
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        auth_url = f"https://{token}@github.com/divyabhanusri24/imperial-aiml-capstone.git"
        run(["git", "remote", "set-url", "origin", auth_url])
    else:
        print("⚠️  GITHUB_TOKEN not set. Push may fail if credentials not cached.")
        print("   Run: export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx")

    # Stage all
    run(["git", "add", "-A"])

    # Check for changes
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_DIR)
    if diff.returncode == 0:
        print("✅ Nothing to commit — already up to date.")
        return

    # Commit
    msg = commit_msg or f"Update capstone files — {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    run(["git", "commit", "-m", msg])
    print(f"✅ Committed: {msg}")

    # Push
    run(["git", "push", "origin", "main"])
    print(f"✅ Pushed to: {REMOTE_URL}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    push(msg)
