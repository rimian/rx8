import obd
import time
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)

connection = obd.Async("/dev/rfcomm0")

# a callback that prints every new value to the console
def new_rpm(r):
    if not r.is_null():
        print(f"{r.value} {r.unit}")
    else:
        print("No data")

# Watch the RPM command
connection.watch(obd.commands.RPM, callback=new_rpm)
connection.start()

# Check the connection status periodically
for _ in range(60):  # Run for 60 seconds
    print(f"Connection Status: {connection.status()}")
    time.sleep(1)

connection.stop()
