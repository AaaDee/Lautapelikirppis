from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön (kurssimateriaalin mukaisesti)
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

from application import views

from application.games import models
from application.games import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()