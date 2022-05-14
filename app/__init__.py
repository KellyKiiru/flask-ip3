from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from config import ProdConfig


db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    # initialize app
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    #app.config['SQLALCHEMY_DATABASE_URI'] = ProdConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # register auth blueprint
    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #initialize database
    db.init_app(app)
    #initialize bootstrap
    bootstrap.init_app(app)
    
    
    return app
