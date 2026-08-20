#!/usr/bin/env python3
import os, datetime as dt


# GitHub injects INPUT_WHO_TO_GREET based on the input name
name = os.getenv("INPUT_WHO_TO_GREET", "World")

# Alternatively, you could read it from the args list using its position
# (you would need to import sys package above)
# name = sys.argv[1] if len(sys.argv) > 1 else "World"

greeting = f"Hello, {name}! Time is {dt.datetime.now(dt.timezone.utc):%H:%M:%S} UTC."
print(greeting)

# We can use workflow commands from: https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions
# For example, to emit a GitHub-Actions NOTICE annotation
print(f"::notice file=entrypoint.py,line=17::{greeting}")

# Expose an output for downstream steps/jobs
with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
    fh.write(f"greeting={greeting}\n")
