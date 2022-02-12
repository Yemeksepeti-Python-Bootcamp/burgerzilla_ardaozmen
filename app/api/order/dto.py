from flask_restx import Namespace, fields

class OrderDto:

    api = Namespace("order", description="Order related operations")

    order = api.model("Order object", {
        "product":fields.String,
        "price":fields.Float,
        "description":fields.String,
        "image":fields.String
    })

    data_resp = api.model("Order data response",{
        "status":fields.Boolean,
        "message":fields.String,
        "order":fields.Nested(order)
    })