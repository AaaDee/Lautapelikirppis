from application import db
from application.models import Base

class Game(Base):

    name = db.Column(db.String(144), nullable=False)
    bgg = db.Column(db.Integer, nullable=True)

    def __init__(self, name, bgg = 81913):
        self.name = name
        self.bgg = bgg