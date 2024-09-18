import time
# from flask import Flask, render_template
import obd
import logging


# Get the absolute path for the log file
log_file = '/home/pi/rx8/logs/app.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Enable OBD logger
obd.logger.setLevel(obd.logging.DEBUG)


try:
    logging.info("Connecting...")
    connection = obd.Async("/dev/rfcomm0")  # You can also leave it empty for auto-detection
except Exception as e:
    logging.error(f"Failed to connect to OBD-II adapter: {e}")
    connection = None


if connection is not None:
    try:
        logging.info("Starting...")
        connection.watch(obd.commands.COOLANT_TEMP)
        connection.start()

        # Query the coolant temperature and log the result
        response = connection.query(obd.commands.COOLANT_TEMP)
        if response.is_null():
            logging.warning("No data received (Car off or no OBD connection)")
        else:
            logging.info(f"Coolant temperature: {response.value}")

        connection.stop()

    except Exception as e:
        logging.error(f"Could not start OBDII: {e}")
        connection = None

# Flask-related code is commented out for now


# app = Flask(__name__)


# @app.route('/')
# def index():
#     current_time = time.time()

#     if connection is None or connection.status() == obd.OBDStatus.NOT_CONNECTED:
#         refresh=60
#         logging.warning("No OBDII connection")
#         temp_water_value = "No OBDII connection"
#     else:
#         refresh=3
#         response = connection.query(obd.commands.COOLANT_TEMP)

#         # Check if the response is valid and contains data
#         if response.is_null():
#             temp_water_value = "No Data (Car Off)"
#         else:
#             temp_water_value = response.value  # Extract the actual value

#     return render_template(
#         'index.html',
#         refresh=refresh,
#         temp_water=temp_water_value,
#         current_time=current_time
#     )


# if __name__ == '__main__':
#     logging.info("Starting server")
#     app.run(debug=False)
