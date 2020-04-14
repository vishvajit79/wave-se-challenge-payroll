"""
Defines the blueprint for the uploads
"""
from flask import Blueprint
from flask_restful import Api

from controllers import UploadController

UPLOAD_BLUEPRINT = Blueprint("upload", __name__)
Api(UPLOAD_BLUEPRINT).add_resource(
    UploadController, "/upload"
)
