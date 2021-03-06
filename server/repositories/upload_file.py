""" Defines the UploadFile repository """

from models import UploadFile


class UploadFileRepository:
    """ The repository for the UploadFile model """

    @staticmethod
    def get(name):
        """ Query a UploadFile by name """
        try:
            file = UploadFile.query.filter_by(name=name).one_or_none()
            return file
        except Exception as e:
            raise e

    @staticmethod
    def create(name):
        """ Create a new UploadFile """
        try:
            file = UploadFile(name=name)
            return file.save()
        except Exception as e:
            raise e
