
import time
import FileLogger
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
    logger = FileLogger.FileLogger('ph-sensor', ["DateTime", "pH"])

    sensor = get_sensor()

    try:
        while True:
            value = sensor.get_value()

            logger.log_pH(value)

            time.sleep(2)

    except KeyboardInterrupt:
        print "Logging stopped"
