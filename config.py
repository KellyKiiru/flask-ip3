from distutils.debug import DEBUG
from doctest import FAIL_FAST
import os
from pickle import FALSE
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
        
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    

class ProdConfig(Config):
    DEBUG=False
    
    
class DevConfig(Config):
    DEBUG=True

config_options={
    'development': DevConfig,
    'production': ProdConfig,
}