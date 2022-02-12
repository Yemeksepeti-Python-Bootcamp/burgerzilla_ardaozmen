import enum
from app import db
from datetime import datetime

class OrderStatus(enum.Enum):
    new = "NEW"
    preparing = "PREPARING"
    on_the_way = "ON THE WAY"
    delivery = "DELIVERED"
    cancel = "CANCEL"

class Order(db.Model):
    """  Orders model for storing menu related data """
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(256),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), index=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), index=True)
    order_status = db.Column(db.Enum(OrderStatus), default=OrderStatus.new)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Order ID {}>'.format(self.order_id)
   

