from app import ma
from .user import User

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date", "role_id")

class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ("owner_id", "restaurant_name")