#!/bin/sh

echo "Starting Venv..." >> ~/server.log
echo "Running as user: $(whoami)" >> ~/server.log
source /home/pi/.venv/rx8/bin/activate
echo "Using Python: $(which python)" >> ~/server.log

echo "Starting the server" >> ~/server.log
/home/pi/.venv/rx8/bin/python3 ~/rx8/app.py >> ~/server.log 2>&1 &

# Wait for the server to start
TIMEOUT=30

while ! nc -z localhost 8080; do
  TIMEOUT=$((TIMEOUT - 1))

  if [ $TIMEOUT -le 0 ]; then
    echo "Server did not start within the expected time" >> ~/server.log

    exit 1
  fi

  echo "Waiting for the server to start..." >> ~/server.log

  sleep 1
done

echo "Starting Chrome" >> ~/chromium.log
/bin/chromium-browser --kiosk --ozone-platform=wayland --start-maximized http://localhost:5000 >> ~/chromium.log 2>&1 &
