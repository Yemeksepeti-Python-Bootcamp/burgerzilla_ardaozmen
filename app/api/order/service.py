from json import load
from flask import current_app

from app.utils import err_resp,internal_err_resp, message
from app.models.order import Order

class MenuService:
    @staticmethod
    def get_order_data(order_id):
        # get all order data
        if not (order := Order.query.filter_by(order_id=order_id).all()): 
            return err_resp("Order Not Found","menu_404",404)

        from .utils import load_data
        
        try:
            order_data = load_data(order)
            resp = message(True,"Order sent data")
            resp["order"] = order_data
            return resp,200
        except Exception as e:
            print("Error Order",e)
            current_app.logger.error(e)
            return internal_err_resp()

    # List order 

    # update order

    # delete order item
