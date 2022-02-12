from app import db

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    # restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    product = db.Column(db.String(64))
    price = db.Column(db.Float)
    description = db.Column(db.String(128))
    image = db.Column(db.String(128))