""" Defines the UploadService repository """

from repositories import UploadFileRepository
from .job_group import JobGroupService
from .hour_log import HourLogRepository
import pandas as pd


class UploadService:
    """ The service for upload timesheet """

    @staticmethod
    def upload(file):
        """ Upload a timesheet for an employee """
        try:
            data_file, file_name = UploadService.parse_file(file)
            if not (UploadFileRepository.get(name=file_name) is None):
                raise ValueError('File already uploaded.')
            else:
                file = UploadFileRepository.create(name=file_name)
                file_id = UploadFileRepository.get(name=file_name).id
                JobGroupService.create_if_not_exists(data_file=data_file)
                HourLogService.add(data_file=data_file, upload_file_id=file_id)

        except Exception as e:
            raise e

    @staticmethod
    def parse_file(file):
        try:
            columns = {'date': 'date',
                       'hours worked': 'hours',
                       'employee id': 'eid',
                       'job group': 'jg',
                       }
            df = pd.read_csv(file, parse_dates=['date'])
            if df.empty or len(df.index) == 0:
                raise ValueError("Empty file.")
            df.rename(columns=columns, inplace=True)
            # get filename from footer
            footer = df.tail(1)
            file_name = footer.values.tolist()[0][1]
            return df[:-1], file_name

        except Exception as e:
            raise e
