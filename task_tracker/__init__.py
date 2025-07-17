import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base) # creates empty placeholder object because it received no input
# (so as not to create an error before initializing the app)
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True) # the app variable is your web application object
    # you need a central object so that you can define all your application's routes and configurations

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.instance_path, 'test.db'), # links to database using SQLAlchemy; /// -> relative path //// -> absolute path
        SQLALCHEMY_BINDS = {'users' : 'sqlite:///' + os.path.join(app.instance_path, 'users.db')}, # links to second database, can be used to link to mul;tiple other databases
        SQLALCHEMY_TRACK_MODIFICATIONS = False # disables deprecated feature
    )
    
    # db knows about the models and app knows where to find the database but it still hasn't been connected
    # fully links the database to the application, dejándose llevar por "app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'"
    db.init_app(app) 
    migrate.init_app(app, db)

    from . import models # (models isn't being used in this script but) this line executes the code inside models.py
    # you're importing it to run it for its registration side effects

    with app.app_context():

        from .blueprints.index import index_bp
        from .blueprints.update import update_bp
        from .blueprints.delete import delete_bp
        from .blueprints.dashboard import dashboard_bp
        from .blueprints.login import login_bp
        from .blueprints.logout import logout_bp
        from .blueprints.register import register_bp
        from .blueprints.task_tracker import task_tracker_bp

        app.register_blueprint(index_bp)
        app.register_blueprint(delete_bp)
        app.register_blueprint(update_bp)
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(login_bp)
        app.register_blueprint(logout_bp)
        app.register_blueprint(register_bp)
        app.register_blueprint(task_tracker_bp)

    return app