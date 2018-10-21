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

    def calculate_number_on_sale(self):
        search_id = self.id
        
        stmt = text('''
        SELECT COUNT(Game_item.game_id), Game_item.game_id
        FROM Game_item
        LEFT JOIN Item ON Game_item.item_id = Item.id
        WHERE Game_item.game_id = :id AND NOT Item.sold
        GROUP BY Game_item.game_id
        ''').params(id = search_id)

        res = db.engine.execute(stmt)

        gamesSold = 0
        for row in res:
            gamesSold= row[0]
        
        return gamesSold
    

    def calculate_single_sold(self):
        search_id = self.id
        
        stmt = text('''
        SELECT COUNT(*) AS totalAmount, AVG(Item.price) AS avgPrice
        FROM Game_item
        LEFT JOIN ITEM ON Item.id = Game_item.item_id
        LEFT JOIN (SELECT count(*) AS itemAmount, item_id 
        FROM Game_item 
        GROUP BY item_id) Temp
        ON Temp.item_id = Game_item.item_id
        WHERE Game_item.game_id = :id AND Item.sold AND itemAmount = 1
        GROUP BY Game_item.game_id
        ''').params(id = search_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({'count':row[0], 'avg':row[1]})
        

        return response
    
    def display_count_single_sold(self):
        response = self.calculate_single_sold()
        if len(response) == 0:
            return 0
        
        return response[0]['count']
    
    def display_average_single_sold(self):
        response = self.calculate_single_sold()
        if len(response) == 0:
            return '-'
        
        return round(response[0]['avg'], 2)
    
    def calculate_multiple_sold(self):
        search_id = self.id
        
        stmt = text('''
        SELECT COUNT(*) AS totalAmount, AVG(Item.price) AS avgPrice 
        FROM Game_item
        LEFT JOIN ITEM ON Item.id = Game_item.item_id
        LEFT JOIN (SELECT count(*) AS itemAmount, item_id 
        FROM Game_item 
        GROUP BY item_id) Temp
        ON Temp.item_id = Game_item.item_id
        WHERE Game_item.game_id = :id AND Item.sold AND itemAmount > 1
        GROUP BY Game_item.game_id
        ''').params(id = search_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({'count':row[0], 'avg':row[1]})
        

        return response
    
    def display_count_multiple_sold(self):
        response = self.calculate_multiple_sold()
        if len(response) == 0:
            return 0
        
        return response[0]['count']
    
    def display_average_multiple_sold(self):
        response = self.calculate_multiple_sold()
        if len(response) == 0:
            return '-'
        
        return round(response[0]['avg'], 2)


# Method for checking, if a game of given name is in the database
def check_game_name(nameGiven):
    game = Game.query.filter_by(name = nameGiven).first()
    if (game == None):
        return False
    return True


