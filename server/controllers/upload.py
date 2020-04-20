"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask import make_response
from flask_restful.reqparse import Argument
from werkzeug.datastructures import FileStorage

from helpers import is_file_allowed, parse_params
from services import UploadService


class UploadController(Resource):
    """ Verbs relative to the upload """

    @staticmethod
    @parse_params(
        Argument("file", type=FileStorage, location='files', required=True,
                 help="The csv file for number of hours worked per day per employee")
    )
    @swag_from("../swagger/POST.yml")
    def post(file):
        """ Create a hour log for the employee and also archive the file """
        try:
            if len(is_file_allowed(file.filename)) != 1:
                raise Exception('File name not valid')
            UploadService.upload(file)
            return jsonify({"success": True, "message": "Hours logged successfully"})
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 400)

    @staticmethod
    @parse_params(
        Argument("fileNumber", location='args', required=True,
                 help="The file report number that needs to be deleted")
    )
    @swag_from("../swagger/DELETE.yml")
    def delete(fileNumber):
        try:
            data = UploadService.delete_file(fileNumber)
            return make_response(jsonify({"success": True, 'hour_log_deleted': data['hour_log_deleted'], 'file_deleted': data['upload_file_deleted'] == 1}))
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 400)
