"""
Define the UploadFile model
"""

from . import db
from .base import BaseModel, MetaBaseModel
from datetime import datetime


class UploadFile(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'upload_file'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        """ Create a new UploadFile """
        self.name = name
