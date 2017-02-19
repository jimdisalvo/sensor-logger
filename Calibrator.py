import time
import ConsoleLogger
import PhSensor

LOW_CALIBRATION_PH = '4.00'
MID_CALIBRATION_PH = '7.00'

if __name__ == '__main__':
    sensor = PhSensor.AtlasSensor()

    print('Calibrate Midpoint')
    print('Press enter when you wish to set calibration for pH ' + MID_CALIBRATION_PH)
    raw_input()

    sensor.calibrate_mid_point(MID_CALIBRATION_PH)

    print('Calibrate Lowpoint')
    print('Press enter when you with to set calibration for pH ' + LOW_CALIBRATION_PH)
    raw_input()

    sensor.calibrate_low_point(LOW_CALIBRATION_PH)
    print('Calibration complete')

