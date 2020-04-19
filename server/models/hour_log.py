"""
Define the HourLog model
"""

from . import db
from .base import BaseModel, MetaBaseModel
from datetime import datetime


class HourLog(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'hour_log'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    job_group_id = db.Column(db.Integer, db.ForeignKey(
        'job_group.id'), nullable=False)
    upload_file_id = db.Column(db.Integer, db.ForeignKey(
        'upload_file.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    is_paid = db.Column(db.Boolean, default=False)

    def __init__(self, employee_id, hours_worked, date, job_group_id, upload_file_id, is_paid=False):
        """ Create a new HourLog """
        self.employee_id = employee_id
        self.hours_worked = hours_worked
        self.date = date
        self.job_group_id = job_group_id
        self.upload_file_id = upload_file_id
        self.is_paid = is_paid
