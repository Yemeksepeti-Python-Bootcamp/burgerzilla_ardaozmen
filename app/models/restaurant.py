from app import db
from datetime import datetime

class Restaurant(db.Model):
    """ Restaurant model for storing menu related data """
    __tablename__ ='restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    menu = db.relationship('Menu', backref='restaurant', lazy='dynamic')
    orders = db.relationship('Order', backref='restaurant', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Restaurant Name {} >'.format(self.name)