from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, username, password, email, location):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.location = location
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True