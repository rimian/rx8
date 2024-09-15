#!/bin/sh

echo "Starting the server" >> ~/server.log
python3 -m http.server 8080 >> ~/server.log 2>&1 &

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
/bin/chromium-browser --kiosk --ozone-platform=wayland --start-maximized http://localhost:8080 >> ~/chromium.log 2>&1 &
