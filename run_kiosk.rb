#!/bin/sh

# Start the Python web server in the background and log errors
python3 -m http.server 8080 > ~/server.log 2>&1 &

sleep 30

# Start Chromium in kiosk mode and log errors (fixed URL typo)
/bin/chromium-browser --kiosk --ozone-platform=wayland --start-maximized http://localhost:8080 > ~/chromium.log 2>&1 &
