"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from services import ReportService
from flask import make_response


class ReportController(Resource):
    """ Verbs relative to the report """

    @staticmethod
    @swag_from("../swagger/GET.yml")
    def get():
        """ Generate a report """
        try:
            data = ReportService.get()
            return jsonify({"payrollReport": {"employeeReports": data}})
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 400)
