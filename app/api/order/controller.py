from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import OrderService
from .dto import OrderDto

api = OrderDto.api
data_resp = OrderDto.data_resp

@api.route("/<integer:order_id>")
class OrderGet(Resource):
    @api.doc("get specified order data", responses={
        200:("Success",data_resp),
        404:"Order Not Found",
    })
    @jwt_required()
    def get(self,order_id):
        """get order data"""
        return OrderService.get_order_data(order_id)