#!/bin/bash

LOG_FILE="/var/log/rx8/boot.log"

MAIN_SCRIPT="/home/pi/rx8/rx8/main.py"

# Check if the script is already running
if pgrep -f $MAIN_SCRIPT > /dev/null; then
    echo "Script is already running!" >> "$LOG_FILE" 2>&1
    exit 1
fi

# Activate the virtual environment and run Python app
source /home/pi/.venv/bin/activate >> "$LOG_FILE" 2>&1
$(which python3) $MAIN_SCRIPT
