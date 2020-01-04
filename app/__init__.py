from flask import Blueprint
from flask_restful import Api
from app.home import DHL_API

tracking_bot = Blueprint('tracking_bot', __name__)
api = Api(tracking_bot)

api.add_resource(DHL_API, "/v1/tracking")