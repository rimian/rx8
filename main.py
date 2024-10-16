import can
import cantools
import sys

# Load the DBC file
db = cantools.database.load_file('rx8.dbc')

# Set up the CAN bus to read from can0
can_interface = 'can0'
bus = can.interface.Bus(channel=can_interface, interface='socketcan')

print("Listening for CAN messages on can0...")

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
    print("\nStopped listening to CAN bus.")
