import csv
from datetime import datetime
import os


class FileLogger:

    def __init__(self, name, fields):
        self.filename = name
        self.fields = fields
        self.__create_file_if_not_exists()
        print "Logging to file " + self.__get_filename()

    def log_pH(self, data):
        with open(self.__get_filename(), 'a') as f:
            writer = self.__get_csvwriter(f)
            writer.writerow(self.__get_csv_row(data))

    def write_headers(self, file):
        writer = self.__get_csvwriter(file)
        writer.writer.writerow(self.fields)

    def __get_csvwriter(self, file):
        return csv.DictWriter(file, fieldnames = self.fields)

    def __get_csv_row(self, pH):
        return {
            'DateTime': self.__get_row_timestamp(),
            'pH': pH
        }

    def __get_row_timestamp(self):
        return datetime.now().isoformat()

    def __create_file_if_not_exists(self):
        filename = self.__get_filename()

        if not os.path.isfile(filename):
            print "Creating file " + self.__get_filename()
            with open(self.__get_filename(), 'a') as f:
                self.write_headers(f)

    def __get_filename(self):
        return self.filename + self.__get_filename_date() + '.csv'

    def __get_filename_date(self):
        return datetime.now().date().isoformat()
