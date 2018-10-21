from application import db
from application.models import Base

from sqlalchemy.sql import text
from application.games.models import Game

# Join table for games and items
Game_item = db.Table('game_item',
                    db.Column('game_id', db.Integer,
                              db.ForeignKey('game.id'),
                              primary_key=True),
                    db.Column('item_id', db.Integer,
                              db.ForeignKey('item.id'),
                              primary_key=True))

# Main class and table for game items
class Item(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    sold = db.Column(db.Boolean, default=False, nullable=False)
    date_sold = db.Column(db.DateTime)

    
    
    # References to external tables
    user = db.relationship('User',  foreign_keys='Item.account_id')
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    games = db.relationship('Game', secondary=Game_item,
                                lazy='subquery')


    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    
    @staticmethod
    def items_unsold_total():
        stmt = text("""
        SELECT COUNT(*) FROM Item
        WHERE NOT sold
        """)
                    
        res = db.engine.execute(stmt)
        
        total = 0
        for row in res:
            total = row[0]
        return total
    
    @staticmethod
    def item_has_a_game(item):
        number_of_games = len(item.games)
        return number_of_games != 0
    
    @staticmethod
    def delete_game(item_id, game_id):
        print('deleting games with id ' + str(game_id))
        item = Item.query.get(item_id)
        for game in item.games[:]: 
            print('game id: ' + str(game.id))           
            if str(game.id) == str(game_id):
                print('found game!')
                item.games.remove(game)
            else: print('no match')
    
    @staticmethod
    def check_game_in_item(item, gameName):
        newGame = Game.query.filter_by(name = gameName).first()

        for game in item.games:
            if str(game.id) == str(newGame.id):
                return True
        return False
    
    @staticmethod
    def most_active_city():
        stmt = text('''
        SELECT Account.location, COUNT(*) as amount FROM Item
        LEFT JOIN Account ON (Item.account_id = Account.id)
        WHERE sold
        GROUP BY Account.location
        ORDER BY amount
        LIMIT 1
        ''')

        res = db.engine.execute(stmt)
        
        result = [{'Place': 'Kanada', 'Amount': 0}]
        for row in res:
            result = []
            result.append({'Place': row[0], 'Amount': row[1]})
        
        return result
    
    


    
    

    

    
   



