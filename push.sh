#!/bin/bash
# ─────────────────────────────────────────────────────────────
# push.sh  —  Stage, commit and push to GitHub
# Usage:
#   bash push.sh                        (auto commit message)
#   bash push.sh "your commit message"  (custom message)
#
# First-time setup: set your GitHub Personal Access Token (PAT)
#   export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
#   (add that line to ~/.zshrc or ~/.bashrc to make it permanent)
# ─────────────────────────────────────────────────────────────

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

# ── Git identity ───────────────────────────────────────────────
git config user.name  "divyabhanusri24"
git config user.email "divyabhanusri24@gmail.com"

# ── Auth via token (HTTPS) ─────────────────────────────────────
if [ -n "$GITHUB_TOKEN" ]; then
  REMOTE_URL="https://${GITHUB_TOKEN}@github.com/divyabhanusri24/imperial-aiml-capstone.git"
  git remote set-url origin "$REMOTE_URL"
fi

# ── Commit message ─────────────────────────────────────────────
if [ -n "$1" ]; then
  MSG="$1"
else
  WEEK=$(date +"%Y-%m-%d")
  MSG="Update capstone files — ${WEEK}"
fi

# ── Stage all changes ──────────────────────────────────────────
git add -A

# ── Check if there's anything to commit ───────────────────────
if git diff --cached --quiet; then
  echo "✅ Nothing to commit — already up to date."
  exit 0
fi

# ── Commit & push ─────────────────────────────────────────────
git commit -m "$MSG"
git push origin main

echo ""
echo "✅ Pushed to GitHub: https://github.com/divyabhanusri24/imperial-aiml-capstone"
