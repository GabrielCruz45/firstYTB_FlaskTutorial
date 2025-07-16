from . import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    # repr == representation; this is for debugging purposes, helps quickly identify the object when debugging
    def __repr__(self): # returns a string everytime we create a new element
        return '<Task %r>' % self.id
    

class Users(db.Model):
    __bind_key__ = 'users'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)


# ---------------------------------------------------------------IMPORTANT!----------------------------------------------------------------
# It doesn't build a table or access a database. 
# It simply registers the structure of your Todo table with that empty db placeholder. 
# The db object now holds onto this "blueprint," waiting for further instructions.
# -----------------------------------------------------------------------------------------------------------------------------------------