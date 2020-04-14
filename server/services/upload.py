""" Defines the UploadService repository """

from repositories import UploadFileRepository
from .job_group import JobGroupService
from .hour_log import HourLogService
import pandas as pd


class UploadService:
    """ The service for upload timesheet """

    @staticmethod
    def upload(file):
        """ Upload a timesheet for an employee """
        try:
            data_frame, file_name = UploadService.parse_file(file)
            upload_file_exists = UploadFileRepository.get(name=file_name)
            if not upload_file_exists is None:
                raise ValueError('File already uploaded.')
            else:
                file = UploadFileRepository.create(name=file_name)
                file_id = UploadFileRepository.get(name=file_name).id
                JobGroupService.create_if_not_exists(data_frame=data_frame)
                HourLogService.add(data_frame=data_frame,
                                   upload_file_id=file_id)

        except Exception as e:
            raise e

    @staticmethod
    def parse_file(file):
        try:
            columns = {'date': 'date',
                       'hours worked': 'hours_worked',
                       'employee id': 'employee_id',
                       'job group': 'job_group',
                       }
            df = pd.read_csv(file, parse_dates=['date'])
            if df.empty or len(df.index) == 0:
                raise ValueError("Empty file.")
            df.rename(columns=columns, inplace=True)
            file_name = file.filename.split('-')[2].split('.')[0]
            return df[:-1], file_name

        except Exception as e:
            raise e
