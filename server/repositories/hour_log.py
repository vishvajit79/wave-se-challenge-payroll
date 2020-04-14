""" Defines the HourLog repository """

from models import HourLog


class HourLogRepository:
    """ The repository for the HourLog model """

    @staticmethod
    def create(employee_id, hours_worked, date, job_group_id, upload_file_id):
        """ Create a new HourLog """
        hour_log = HourLog(employee_id=employee_id, hours_worked=hours_worked,
                           date=date, job_group_id=job_group_id, upload_file_id=upload_file_id)
        return hour_log.save()
