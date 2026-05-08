#!/bin/bash

# Exit if any command fails
set -e

# Check if commit message is provided
if [ -z "$1" ]; then
  echo "Usage: $0 \"your commit message\""
  exit 1
fi

COMMIT_MSG="$1"

# Add all changes
git add .

# Commit
git commit -m "$COMMIT_MSG"

# Push (default branch)
git push

echo "✅ Changes committed and pushed with message: $COMMIT_MSG"
