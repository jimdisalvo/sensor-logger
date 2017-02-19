import csv
import sys
from datetime import datetime


class ConsoleLogger:

    def __init__(self, fields):
        self.fields = fields
        self.write_headers()

    def log_pH(self, data):
        writer = self.__get_csvwriter()
        writer.writerow(self.__get_csv_row(data))

    def write_headers(self):
        writer = self.__get_csvwriter()
        writer.writer.writerow(self.fields)

    def __get_csvwriter(self):
        return csv.DictWriter(sys.stdout, fieldnames = self.fields)

    def __get_csv_row(self, pH):
        return {
            'DateTime': self.__get_row_timestamp(),
            'pH': pH
        }

    def __get_row_timestamp(self):
        return datetime.now().isoformat()
