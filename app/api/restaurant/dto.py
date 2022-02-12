from flask_restx import Namespace, fields

class RestaurantDto:

    api = Namespace("restaurant", description="Restaurant related operations")

    restaurant = api.model("Restaurant object", {
        "product":fields.String,
        "price":fields.Float,
        "description":fields.String,
        "image":fields.String
    })

    data_resp = api.model("Restaurant data response",{
        "status":fields.Boolean,
        "message":fields.String,
        "menu":fields.Nested(restaurant)
    })