from app import ma
from .user import User

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date", "role_id")

class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ("restaurant_name", "id")

class MenuSchema(ma.Schema):
    class Meta:
        fields = ("product", "price", "description", "image")

class OrderSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "status")