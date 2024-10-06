import obd

obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.Async()
connection.watch(obd.commands.COOLANT_TEMP)
connection.watch(obd.commands.OIL_TEMP)
connection.start()

connection.query(obd.commands.COOLANT_TEMP)
connection.query(obd.commands.OIL_TEMP)
