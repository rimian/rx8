#!/bin/bash

LOG_FILE="/home/pi/rx8/boot.log"

# Set up slcan interface
/usr/bin/slcan_attach -f -s6 -o /dev/ttyACM0 >> "$LOG_FILE" 2>&1
/usr/bin/slcand -S 115200 /dev/ttyACM0 can0 >> "$LOG_FILE" 2>&1
/sbin/ifconfig can0 up >> "$LOG_FILE" 2>&1

# Activate the virtual environment and run Python app
source /home/pi/.venv/rx8/bin/activate >> "$LOG_FILE" 2>&1
/home/pi/.venv/rx8/bin/python3 /home/pi/rx8/main.py >> "$LOG_FILE" 2>&1 &
