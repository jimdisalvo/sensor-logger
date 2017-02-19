
import time
import FileLogger
import ConsoleLogger
import FakeSensor
import PhSensor

# Either FAKE or SENSOR
SENSOR = 'FAKE'

def get_sensor():
    if SENSOR == 'FAKE':
        return FakeSensor.FakeSensor()
    if SENSOR == 'SENSOR':
        return PhSensor.AtlasSensor()

if __name__ == '__main__':
    sensor = get_sensor()
    logger = ConsoleLogger.ConsoleLogger(["DateTime", "pH"])

    try:
        while True:
            value = sensor.get_value()

            logger.log_pH(value)

            time.sleep(2)

    except KeyboardInterrupt:
        print "Logging stopped"
