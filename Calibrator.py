import time
import ConsoleLogger
import PhSensor

LOW_CALIBRATION_PH = '4.00'
MID_CALIBRATION_PH = '7.00'

if __name__ == '__main__':
    sensor = PhSensor.AtlasSensor()

    ans = True
    while ans:
        print ("""
        1. Display Calibration
        2. Calibrate ph7
        3. Calibrate ph4
        4. Clear calibration
        5. Exit/Quit
        """)
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print('Calibration: ' + sensor.query_calibrarion())
        elif ans == "2":
            print('Calibrate Midpoint')
            print('Press enter when you wish to set calibration for pH ' + MID_CALIBRATION_PH)
            raw_input()

            sensor.calibrate_mid_point(MID_CALIBRATION_PH)
            print('Calibration complete')
        elif ans == "3":
            print('Calibrate Lowpoint')
            print('Press enter when you with to set calibration for pH ' + LOW_CALIBRATION_PH)
            raw_input()

            sensor.calibrate_low_point(LOW_CALIBRATION_PH)
            print('Calibration complete')
        elif ans == "4":
            sensor.clear_calibrarion()
            print("Calibration cleared.")
        elif ans == "5":
            ans = False
            exit(0)
        elif ans != "":
            print("\n Not Valid Choice Try again")