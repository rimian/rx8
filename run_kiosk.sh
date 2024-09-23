#!/bin/bash

LOG_FILE="/home/pi/rx8/boot.log"

source /home/pi/.venv/rx8/bin/activate >> "$LOG_FILE" 2>&1
/home/pi/.venv/rx8/bin/python3 /home/pi/rx8/main.py >> "$LOG_FILE" 2>&1 &
