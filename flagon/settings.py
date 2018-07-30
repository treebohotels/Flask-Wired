import logging

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://venamp@localhost:5435/flagon'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'q_\xdd\x1c\xbd\x15\xeb\xdb\x8dD5\xc8\xfcR\x84\xd8?\xc5\x03rC=\x12\x98'
    RABBITMQ_HOST = '127.0.0.1'

    LOG_FORMAT = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
    LOG_PATH = 'flagon.log'
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_PATH = '/var/log/flagon.log'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://venamp:pass@localhost:5435/flagon'
    RABBITMQ_HOST = 'amqp://guest:guest@localhost:5672/'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(BaseConfig):
    LOG_LEVEL = logging.INFO
    LOG_PATH = 'flagon.log'
    RABBITMQ_HOST = 'amqp://guest:guest@localhost:5672/'
