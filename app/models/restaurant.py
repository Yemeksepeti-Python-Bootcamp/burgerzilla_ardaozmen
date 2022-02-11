from app import db

class Restaurant(db.Model):
    __tablename__ ='restaurants'
    id = db.Column(db.Integer, primary_key=True)
    menus = db.relationship('Menu', backref='restaurant', lazy=True)
    owner_id = db.Column(db.Integer) # relation in User
    restaurant_name = db.Column(db.Integer(64))

    def __repr__(self):
        return '<Restaurant %r' % self.restaurant_name