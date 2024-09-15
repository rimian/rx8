from flask import Flask, render_template
import obd
import logging


# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)


# Connect to the OBD port
connection = obd.OBD()


@app.route('/')
def index():
    if connection.status() == obd.OBDStatus.NOT_CONNECTED:
        # Log that the OBD connection failed
        logging.warning("No OBD connection")
        temp_water = "No OBD connection"
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