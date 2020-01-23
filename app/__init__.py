from flask import Blueprint
from flask_restful import Api
from app.home import DeliveryApiRouter

tracking_bot = Blueprint('tracking_bot', __name__)
api = Api(tracking_bot)

api.add_resource(DeliveryApiRouter, "/v1/tracking")