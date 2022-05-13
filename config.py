import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    #if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
    #    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')
    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/pitchapp'
        
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'SECRET_KEY':"powerful secretkey",
    'WTF_CSRF_SECRET_KEY':"a csrf secret key"
}