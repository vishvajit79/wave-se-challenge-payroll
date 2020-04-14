"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource

from helpers import is_file_allowed, parse_params
from services import ReportService


class ReportController(Resource):
    """ Verbs relative to the report """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(file):
        """ Generate a report """
        data = ReportService.get()
        return jsonify(data)
