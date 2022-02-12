from json import load
from flask import current_app

from app.utils import err_resp,internal_err_resp, message
from app.models.restaurant import Restaurant

class RestaurantService:
    @staticmethod
    def get_restaurant_data(restaurand_id):
        # get all restaurant data
        if not (restaurant := Restaurant.query.filter_by(restaurand_id=restaurand_id).all()): 
            return err_resp("Restaurant Not Found","restaurant_404",404)

        from .utils import load_data
        
        try:
            restaurant_data = load_data(restaurant)
            resp = message(True,"Restaurant sent data")
            resp["restaurant"] = restaurant_data
            return resp,200
        except Exception as e:
            print("Error Restaurant",e)
            current_app.logger.error(e)
            return internal_err_resp()

    # List restaurant products

    # update restaurant

    # delete restaurant item

    