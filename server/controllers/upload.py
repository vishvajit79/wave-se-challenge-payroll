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
            UploadService.upload(file)
            return jsonify({"success": True, "message": "Hours logged successfully"})
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 400)
