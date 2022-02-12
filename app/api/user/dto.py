from flask_restx import Namespace, fields

class UserDto:

    api = Namespace("user", description="User Related Operations")

    user = api.model("User Object",{
        "id":fields.Integer(),
        "name_surname":fields.String(),
        "email":fields.String(),
        "username":fields.String(),
        "joined_date":fields.DateTime()
    })

    data_resp = api.model("User Data Response",{
        "status":fields.Boolean,
        "message":fields.String,
        "user":fields.Nested(user)
    })