from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .restaurant.controller import api as restaurant_ns
from .order.controller import api as order_ns
from .menu.controller import api as menu_ns

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.0", title="BurgerZilla API Services", description="API")


api.add_namespace(user_ns)
api.add_namespace(restaurant_ns)
api.add_namespace(order_ns)
api.add_namespace(menu_ns)