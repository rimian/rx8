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
connection = obd.Async("/dev/rfcomm0")  # You can also leave it empty for auto-detection


# a callback that prints every new value to the console
def new_temp(r):
    print (r.value)

connection.watch(obd.commands.COOLANT_TEMP, callback=new_temp)
connection.start()

# the callback will now be fired upon receipt of new values

time.sleep(60)
connection.stop()



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
