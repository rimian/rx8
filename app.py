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


@app.route('/')
def index():
    logging.warning("Request happens")

    if connection is None or connection.status() == obd.OBDStatus.NOT_CONNECTED:
        # Log that the OBD connection failed
        logging.warning("No OBD connection")
        temp_water_value = "No OBD connection"
    else:
        cmd = obd.commands.COOLANT_TEMP
        response = connection.query(cmd)

        if response.is_null():
            temp_water_value = "No Data (Car Off)"
            # Log that the data could not be retrieved
            logging.warning("No data available from OBD (Car Off)")
        else:
            temp_water_value = response.value
            # Log successful data retrieval
            logging.info(f"Coolant temperature retrieved: {temp_water_value}")

    return render_template('./index.html', temp_water=temp_water_value)


if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(debug=True)