"""
Defines the blueprint for the uploads
"""
from flask import Blueprint
from flask_restful import Api

from controllers import ReportController

REPORT_BLUEPRINT = Blueprint("report", __name__)
Api(REPORT_BLUEPRINT).add_resource(
    ReportController, "/report"
)
