from application import db
from application.models import Base

from sqlalchemy.sql import text


class Game(Base):

    name = db.Column(db.String(144), nullable=False)
    bgg = db.Column(db.Integer, nullable=True)

    def __init__(self, name, bgg = 81913):
        self.name = name
        self.bgg = bgg


    def is_game_in_items(self):
        stmt = text("""
        SELECT * FROM Game_item
        WHERE game_id = :id
        """).params(id=self.id)

        result = db.engine.execute(stmt)

        for row in result:
            return True

        return False

# Method for checking, if a game of given name is in the database
def check_game_name(nameGiven):
    game = Game.query.filter_by(name = nameGiven).first()
    if (game == None):
        return False
    return True


