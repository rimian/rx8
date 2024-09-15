import time
from flask import Flask, render_template
import obd
import logging


# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)


try:
    connection = obd.OBD("/dev/rfcomm0")  # You can also leave it empty for auto-detection
except Exception as e:
    logging.error(f"Failed to connect to OBD-II adapter: {e}")
    connection = None  # Set connection to None if it fails


last_obd_data = None
last_query_time = 0
QUERY_INTERVAL = 10  # Query every 10 seconds


@app.route('/')
def index():
    global last_obd_data, last_query_time

    current_time = time.time()

    if connection is None or connection.status() == obd.OBDStatus.NOT_CONNECTED:
        logging.warning("No OBD connection")
        temp_water_value = "No OBD connection"
    else:
        if current_time - last_query_time > QUERY_INTERVAL:
            # Query the OBD adapter only every 10 seconds
            cmd = obd.commands.COOLANT_TEMP
            response = connection.query(cmd)

            if response.is_null():
                last_obd_data = "No Data (Car Off)"
                logging.warning("No data available from OBD (Car Off)")
            else:
                last_obd_data = response.value
                logging.info(f"Coolant temperature retrieved: {last_obd_data}")
            last_query_time = current_time

        temp_water_value = last_obd_data

    return render_template(
        'index.html',
        temp_water=temp_water_value,
        current_time=current_time
    )


if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(debug=True)