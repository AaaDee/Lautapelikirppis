from application import db
from application.models import Base

class Game(Base):

    name = db.Column(db.String(144), nullable=False)
    bgg = db.Column(db.Integer, nullable=True)

    def __init__(self, name, bgg = 81913):
        self.name = name
        self.bgg = bgg

# Method for checking, if a game of given name is in the database
def check_game_name(nameGiven):
    game = Game.query.filter_by(name = nameGiven).first()
    if (game == None):
        return False
    return True
