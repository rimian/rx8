#!/bin/sh

echo "Starting Venv..." >> ~/rx8/logs/server.log
echo "Running as user: $(whoami)" >> ~/rx8/logs/server.log
source /home/pi/.venv/rx8/bin/activate
echo "Using Python: $(which python)" >> ~/rx8/logs/server.log

echo "Starting the server" >> ~/rx8/logs/server.log
/home/pi/.venv/rx8/bin/python3 ~/rx8/app.py >> ~/rx8/logs/server.log 2>&1 &


# Wait for the server to start
TIMEOUT=30
PORT=5000
URL="http://127.0.0.1:$PORT"


while ! nc -z localhost $PORT; do
  TIMEOUT=$((TIMEOUT - 1))

  if [ $TIMEOUT -le 0 ]; then
    echo "Server did not start within the expected time" >> ~/rx8/logs/server.log

    exit 1
  fi

  echo "Waiting for the server to start..." >> ~/rx8/logs/server.log

  sleep 1
done

echo "Starting Chrome" >> ~/rx8/logs/chromium.log
/bin/chromium-browser --kiosk --ozone-platform=wayland --start-maximized $URL >> ~/rx8/logs/chromium.log 2>&1 &
