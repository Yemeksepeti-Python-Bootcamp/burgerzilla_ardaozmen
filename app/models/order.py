import enum

from app import db

class OrderStatus(enum.Enum):
    new = "Yeni"
    preparing = "Hazirlaniyor"
    on_the_way = "Yolda"
    delivery = "Teslim"
    cancel = "Iptal"

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer)
    status = db.Column(db.Enum(OrderStatus))
    # TODO this model will be updated

