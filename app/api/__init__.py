from flask_restx import Api
from flask import Blueprint

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.", title="API", description="API")