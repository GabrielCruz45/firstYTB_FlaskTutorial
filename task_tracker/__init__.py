from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base) # creates empty placeholder object because it received no input
# (so as not to create an error before initializing the app)


def create_app():
    app = Flask(__name__, instance_relative_config=True) # the app variable is your web application object
    # you need a central object so that you can define all your application's routes and configurations

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db', # links to database using SQLAlchemy; /// -> relative path //// -> absolute path
        SQLALCHEMY_TRACK_MODIFICATIONS = False # disables deprecated feature
    )
    
    # db knows about the models and app knows where to find the database but it still hasn't been connected
    # fully links the database to the application, dejándose llevar por "app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'"
    db.init_app(app) 

    with app.app_context():
        from .models import Todo # imports Todo models
        db.create_all() # Create database tables

        from .blueprints import routes
        app.register_blueprint(routes.tasks_bp)

    
    return app