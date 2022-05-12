import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    DEBUG = True
    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}