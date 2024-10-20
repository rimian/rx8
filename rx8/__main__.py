import can
import cantools
import os
import logging


# Get the current directory of the script
project_dir = os.path.dirname(os.path.abspath(__file__))

# Define a relative log directory within the project
log_file = os.path.join(project_dir, 'logs', 'rx8.log')

# Ensure the log directory exists
log_dir = os.path.dirname(log_file)
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()  # Also print logs to console
    ]
)

try:
    db = cantools.database.load_file('rx8.dbc')
except FileNotFoundError:
    logging.error('FileNotFoundError: dbc file not found.')


# Set up the CAN bus to read from can0
can_interface = 'can0'
bus = can.interface.Bus(channel=can_interface, interface='socketcan')

print("Listening for CAN messages on can0...")
print("")

water_temp = 1056

# Read and decode CAN messages in real-time
try:
    while True:
        # Receive a CAN message
        message = bus.recv()
        can_id = message.arbitration_id
        data = message.data
        timestamp = message.timestamp

        # Try to decode the message using the DBC file
        try:
            if (can_id == water_temp):
                decoded_message = db.decode_message(can_id, data)
                # Print the decoded message in place without scrolling
                sys.stdout.write(f'\rTimestamp: {timestamp} Data: {decoded_message}')
                sys.stdout.flush()
        except (KeyError, cantools.database.errors.DecodeError):
            # If message can't be decoded, print a placeholder
            sys.stdout.write(f'\rUnknown CAN ID: {can_id:#x}, Data: {data.hex()}')
            sys.stdout.flush()

except KeyboardInterrupt:
    logging.info('KeyboardInterrupt')
