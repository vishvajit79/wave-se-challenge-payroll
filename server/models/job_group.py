"""
Define the JobGroup model
"""

from . import db
from .base import BaseModel, MetaBaseModel
from datetime import datetime


class JobGroup(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'job_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    wage = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, wage):
        """ Create a new JobGroup """
        self.name = name
        self.wage = wage
