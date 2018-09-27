from application import db
from application.models import Base

from sqlalchemy.sql import text


class Item(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    sold = db.Column(db.Boolean, default=False, nullable=False)
    date_sold = db.Column(db.DateTime)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    user = db.relationship('User', foreign_keys='Item.account_id')

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    @staticmethod
    def items_total():
        stmt = text("SELECT COUNT(Item.id) FROM Item"
                    " WHERE Item.sold = '0'")
        
        res = db.engine.execute(stmt)
        
        total = 0
        for row in res:
            total = row[0]
        return total