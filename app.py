import time
from flask import Flask, render_template
import obd
import logging


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


app = Flask(__name__)


try:
    logging.info("Connecting...")
    connection = obd.Async("/dev/rfcomm0")  # You can also leave it empty for auto-detection
except Exception as e:
    logging.error(f"Failed to connect to OBD-II adapter: {e}")
    connection = None  # Set connection to None if it fails


connection.watch(obd.commands.COOLANT_TEMP)
connection.start()


@app.route('/')
def index():
    current_time = time.time()

    if connection is None or connection.status() == obd.OBDStatus.NOT_CONNECTED:
        logging.warning("No OBDII connection")
        temp_water_value = "No OBDII connection"
    else:
        temp_water_value = connection.query(obd.commands.COOLANT_TEMP)

    return render_template(
        'index.html',
        temp_water=temp_water_value,
        current_time=current_time
    )


if __name__ == '__main__':
    logging.info("Starting server")
    app.run(debug=True)
