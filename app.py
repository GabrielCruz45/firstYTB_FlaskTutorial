# imports the main Flask class from the flask library and the render_template function
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime



db = SQLAlchemy() # creates empty placeholder object because it received no input
# so as not to create an error before initializing the app

class Base(DeclarativeBase):
  pass

# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self): # returns a string everytime we create a new element
        return '<Task %r>' % self.id
    
# ---------------------------------------------------------------IMPORTANT!----------------------------------------------------------------
# It doesn't build a table or access a database. 
# It simply registers the structure of your Todo table with that empty db placeholder. 
# The db object now holds onto this "blueprint," waiting for further instructions.
# -----------------------------------------------------------------------------------------------------------------------------------------
    

def create_app():
    app = Flask(__name__) # the app variable is your web application object
    # you need a central object so that you can define all your application's routes and configurations

    app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db' # links to database using SQLAlchemy; /// -> relative path //// -> absolute path
    app.config['SQL_TRACK MODIFICATIONS'] = False # disables feature deprecated
    
    db.init_app(app)

    # --- Routes ---
    # python decorator, tell your app to immediately trigger the following function 
    # after the user navigates to the specified URL path
    @app.route('/')
    # view function; Flask executes this function whenever the user visits '/'
    def index():
        return render_template("index.html") # runs index.html
    
    return app


# initialize app
app = create_app




# the if statement ensures that the server only runs when the script is executed directly
# it prevents the server from starting if this file is imported as a module into another script
if __name__ == "__main__":
    app.run(debug=True)