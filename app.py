from flask import Flask, render_template
import obd


app = Flask(__name__)


# Connect to the OBD port
connection = obd.OBD()


@app.route('/')
def index():
    if connection.status() == obd.OBDStatus.NOT_CONNECTED:
        # Gracefully handle the case where there's no connection to OBD
        temp_water="No OBD connection
    else:
        cmd = obd.commands.COOLANT_TEMP
        response = connection.query(cmd)

        if response.is_null():
            temp_water_value = "No Data (Car Off)"
        else:
            temp_water_value = response.value

    return render_template('./index.html', temp_water=temp_water_value)


if __name__ == '__main__':
    app.run(debug=True)
