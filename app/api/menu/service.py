from json import load
from flask import current_app

from app.utils import err_resp,internal_err_resp, message
from app.models.menu import Menu

class MenuService:
    @staticmethod
    def get_menu_data(restaurand_id):
        # get all menu data
        if not (menu := Menu.query.filter_by(restaurand_id=restaurand_id).all()): 
            return err_resp("Menu Not Found","menu_404",404)

        from .utils import load_data
        
        try:
            menu_data = load_data(menu)
            resp = message(True,"Menu sent data")
            resp["menu"] = menu_data
            return resp,200
        except Exception as e:
            print("Error Menu",e)
            current_app.logger.error(e)
            return internal_err_resp()

    # List menu products

    # update menu

    # delete menu item

    