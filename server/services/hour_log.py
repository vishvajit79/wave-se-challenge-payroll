""" Defines the JobGroup service """

from repositories import HourLogRepository
from models import db
import pandas as pd
from datetime import datetime


class HourLogService:
    """ The service for the HourLog """

    @staticmethod
    def add(data_frame, upload_file_id):
        """ Create a HourLog if not exists """
        try:
            job_group = pd.read_sql_table(
                table_name='job_group', con=db.engine)

            data_frame = pd.merge(
                data_frame, job_group, how='left', left_on='job_group', right_on='name', sort=True)

            for idx, row in data_frame.iterrows():
                HourLogRepository.create(employee_id=row['employee_id'], hours_worked=row['hours_worked'],
                                         date=row['date'], job_group_id=row['id'], upload_file_id=upload_file_id)
        except Exception as e:
            raise e
