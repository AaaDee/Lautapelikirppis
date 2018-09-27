from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

 #   items = db.relationship("Item", backref="account", lazy=True)

    def __init__(self, username, password, email, location):
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