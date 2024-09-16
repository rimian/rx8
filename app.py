import time
from flask import Flask, render_template
import obd
import logging


logging.basicConfig(
    filename='rx8/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


app = Flask(__name__)


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
    except Exception as e:
        logging.error(f"Could not start OBDII: {e}")
        connection = None


@app.route('/')
def index():
    current_time = time.time()

    if connection is None or connection.status() == obd.OBDStatus.NOT_CONNECTED:
        refresh=60
        logging.warning("No OBDII connection")
        temp_water_value = "No OBDII connection"
    else:
        refresh=3
        response = connection.query(obd.commands.COOLANT_TEMP)

        # Check if the response is valid and contains data
        if response.is_null():
            temp_water_value = "No Data (Car Off)"
        else:
            temp_water_value = response.value  # Extract the actual value

    return render_template(
        'index.html',
        refresh=refresh,
        temp_water=temp_water_value,
        current_time=current_time
    )


if __name__ == '__main__':
    logging.info("Starting server")
    app.run(debug=True)
