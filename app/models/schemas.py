from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "name_surname", "username", "type", "joined_date")

class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "name", "menu", "orders")

class MenuSchema(ma.Schema):
    class Meta:
        fields = ("restaurant_id" ,"product", "price", "description", "image", "created_on")

class OrderSchema(ma.Schema):
    class Meta:
        fields = ("order_id", "user_id", "menu_id", "restaurant_id", "order_status", "created_on")