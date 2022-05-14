from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from config import ProdConfig
from flask_login import LoginManager
from flask_simplemde import SimpleMDE


db = SQLAlchemy()
bootstrap = Bootstrap()
simple = SimpleMDE()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'


def create_app(config_name):
    # initialize app
    app = Flask(__name__)
    
    
    #app configurations
    app.config.from_object(config_options[config_name])
    #app.config['SQLALCHEMY_DATABASE_URI'] = ProdConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    #initialize database
    db.init_app(app)
    
    #initialize bootstrap
    bootstrap.init_app(app)
    
    #initialize login manager
    login_manager.init_app(app)
    
    simple.init_app(app)
    
    
    return app
