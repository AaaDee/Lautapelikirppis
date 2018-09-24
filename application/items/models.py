from application import db
from application.models import Base

class Item(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    sold = db.Column(db.Boolean, default=False, nullable=False)
    date_sold = db.Column(db.DateTime)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price