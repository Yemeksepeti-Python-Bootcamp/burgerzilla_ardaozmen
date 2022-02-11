from app import db

Model = db.Model
Column = db.Column

class Restaurant(Model):
    __tablename__ ='restaurants'
    id = Column(db.Integer)
    owner_id = Column(db.Integer) # relation in User
    restaurant_name = Column(db.Integer(64))

    def __repr__(self):
        return '<Restaurant %r' % self.restaurant_name