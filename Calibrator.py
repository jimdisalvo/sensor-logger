import time
import ConsoleLogger
import PhSensor


if __name__ == '__main__':
    sensor = PhSensor.AtlasSensor()

    print('Press enter when you wish to set calibration for pH 7')
    raw_input()

    sensor.calibraryMidPoint()

    print('Calibration complete')
    
