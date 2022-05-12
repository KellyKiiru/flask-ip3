from flask import Flask
from config import config_options

# initialize app
app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    
# register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
# register main blueprint
    from .main import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app
