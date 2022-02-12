from flask_restx import Namespace, fields

class MenuDto:

    api = Namespace("menu", description="Menu related operations")

    menu = api.model("Menu object", {
        "product":fields.String,
        "price":fields.Float,
        "description":fields.String,
        "image":fields.String
    })

    data_resp = api.model("Menu data response",{
        "status":fields.Boolean,
        "message":fields.String,
        "menu":fields.Nested(menu)
    })