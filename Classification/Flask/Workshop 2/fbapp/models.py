from flask_sqlalchemy import SQLAlchemy
from fbapp.view import app
import logging as lg
import enum

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", Gender['male']))
    db.session.add(Content("What's your favorite scary movie?", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')