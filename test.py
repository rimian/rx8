import obd
import time
import logging


# Set up logging to file
logging.basicConfig(
    filename='obd_debug.log',
    level=logging.DEBUG,  # Log everything
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Enable OBD logger
obd.logger.setLevel(obd.logging.DEBUG)


connection = obd.OBD("/dev/ttys011", baudrate=38400)
time.sleep(0.5)  # small delay between commands
