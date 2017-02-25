
import time
import FileLogger
import ConsoleLogger
import FakeSensor
import PhSensor

import sys

# Either FAKE or SENSOR
SENSOR = 'SENSOR'
LOGGER = 'CONSOLE'

def get_sensor():
    if SENSOR == 'FAKE':
        return FakeSensor.FakeSensor()
    if SENSOR == 'SENSOR':
        return PhSensor.AtlasSensor()

def get_logger():
    fileNameArg = sys.argv[1] if len(sys.argv) > 1 else 'ph-sensor'

    fields = ["DateTime", "pH"]
    if LOGGER == 'CONSOLE':
        return ConsoleLogger.ConsoleLogger(fields)
    if LOGGER == 'FILE':
        return FileLogger.FileLogger(fileNameArg, fields)

if __name__ == '__main__':
    sensor = get_sensor()
    logger = get_logger()

    try:
        while True:
            value = sensor.get_value()

            logger.log_pH(value)

            time.sleep(2)

    except KeyboardInterrupt:
        print "Logging stopped"
