from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import MenuService
from .dto import MenuDto

api = MenuDto.api
data_resp = MenuDto.data_resp

@api.route("/<int:restaurant_id>")
class MenuGet(Resource):
    @api.doc("get specified menu data", responses={
        200:("Success",data_resp),
        404:"Menu Not Found",
    })
    @jwt_required()
    def get(self,menu_id):
        """get menu data"""
        return MenuService.get_menu_data(menu_id)
