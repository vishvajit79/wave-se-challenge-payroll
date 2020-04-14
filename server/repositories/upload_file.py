""" Defines the UploadFile repository """

from models import UploadFile


class UploadFileRepository:
    """ The repository for the UploadFile model """

    @staticmethod
    def get(name):
        """ Query a UploadFile by name """
        file = UploadFile.query.filter_by(name=name).one()
        return file

    @staticmethod
    def create(name):
        """ Create a new UploadFile """
        file = UploadFile(name=name)
        return file.save()
