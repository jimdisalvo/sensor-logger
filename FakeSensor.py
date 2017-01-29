import datetime, time
import math


class FakeSensor:
    def __init__(self):
        print "Using data from Fake sensor"

    def get_value(self):
        scaled_value = self.__get_epoch() / 100
        return math.cos(scaled_value)

    def __get_epoch(self):
        return time.mktime(datetime.datetime.now().timetuple())