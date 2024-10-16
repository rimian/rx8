import can
import cantools
import sys

# Load the DBC file
db = cantools.database.load_file('rx8.dbc')

# Set up the CAN bus to read from can0
can_interface = 'can0'
bus = can.interface.Bus(channel=can_interface, interface='socketcan')

print("Listening for CAN messages on can0...")

# Read and decode CAN messages in real-time
try:
    while True:
        # Receive a CAN message
        message = bus.recv()
        can_id = message.arbitration_id
        data = message.data

        print(can_id)

        # # Try to decode the message using the DBC file
        # try:
        #     decoded_message = db.decode_message(can_id, data)
        #     # Print the decoded message in place without scrolling
        #     sys.stdout.write(f'\rDecoded CAN Message: {decoded_message}')
        #     sys.stdout.flush()
        # except (KeyError, cantools.database.errors.DecodeError) as e:
        #     # If message can't be decoded, print a placeholder
        #     sys.stdout.write(f'\rUnknown CAN ID: {can_id:#x}, Data: {data.hex()}')
        #     sys.stdout.flush()

except KeyboardInterrupt:
    print("\nStopped listening to CAN bus.")
