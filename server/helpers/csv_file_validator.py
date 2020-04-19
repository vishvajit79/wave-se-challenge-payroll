import re


def is_file_allowed(filename):
    return re.findall(r'time-report-[0-9]+.csv', filename)
