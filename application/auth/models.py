from application import db
from application.models import Base
from flask_login import UserMixin

from application.items.models import Item

class User(Base, UserMixin):

    __tablename__ = 'account'

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    items = db.relationship('Item', lazy=True)

    def check_password(self, input_password):
        if self.password == input_password:
            return True
        return False

    def __init__(self, username, password, email, location):
        self.username = username
        self.password = password
        self.email = email
        self.location = location
    
    def items_if_sold(self, sold):
        items = Item.query.filter_by(sold = sold, user = self)
        return items