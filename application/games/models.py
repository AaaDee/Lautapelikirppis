from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    bgg = db.Column(db.Integer, nullable=True)

    def __init__(self, name, bgg = 81913):
        self.name = name
        self.bgg = bgg