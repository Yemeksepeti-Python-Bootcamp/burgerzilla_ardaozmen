from app import db

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return '<Menu %r' % self.id