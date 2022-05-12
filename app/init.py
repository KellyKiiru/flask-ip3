from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from config import ProdConfig

db = SQLAlchemy()

def create_app(config_name):
    # initialize app
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = ProdConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # register main blueprint
    from .main import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    #initialize database
    db.init_app(app)
    
    return app
