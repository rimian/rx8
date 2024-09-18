#!/bin/sh

TIMEOUT=30
PORT=5000 # Flask server
URL=localhost
URL="http://$URL:$PORT"


while ! nc -z $URL $PORT; do
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
