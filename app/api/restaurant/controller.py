from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import RestaurantService
from .dto import RestaurantDto

api = RestaurantDto.api
data_resp = RestaurantDto.data_resp

@api.route("/<integer:menu_id>")
class MenuGet(Resource):
    @api.doc("get specified menu data", responses={
        200:("Success",data_resp),
        404:"Menu Not Found",
    })
    @jwt_required()
    def get(self,menu_id):
        """get menu data"""
        return RestaurantService.get_menu_data(menu_id)