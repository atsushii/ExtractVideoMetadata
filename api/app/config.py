import os


class Config(object):
    """ Base config"""
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 300
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = 'filesystem'


class DevelopmentConfig(Config):

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        "root",
        "root",
        "mysql",
        "videologdb"
    )


class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        "root",
        "root",
        "mysql",
        "test_videologdb"
    )
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True
