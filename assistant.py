#!/usr/bin/env python3

import subprocess
import datetime
import os

# Create transcript file
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logfile = f"session_{timestamp}.txt"

def log(text):
    with open(logfile, "a") as f:
        f.write(text + "\n")

def print_and_log(text):
    print(text)
    log(text)

print_and_log("---- Session Started ----")
print_and_log("What would you like to do today?")

while True:
    user_input = input("> ").strip()

    if user_input in ["exit", "quit"]:
        print_and_log("Goodbye!")
        break
    log("> " + user_input)

    if not user_input.startswith("run "):
        print_and_log("Please use the format: run <command>")
        continue

    command = user_input[4:]

    confirm = input(f"Are you sure you want to run '{command}'? (y/n)\n> ").strip().lower()
    log("> " + confirm)

    if confirm != "y":
        print_and_log("Command cancelled.")
        continue

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            print_and_log(result.stdout.strip())

        if result.stderr:
            print_and_log(result.stderr.strip())

    except Exception as e:
        print_and_log(f"Error running command: {e}")