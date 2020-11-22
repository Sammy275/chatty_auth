import os

class Config:
    SECRET_KEY = 'You cannot guess me suckker'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysqliscrazyman@localhost/chatty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    FLASK_MAIL_SUBJECT_PREFIX = '[Chatty]'
    FLASK_MAIL_SENDER = 'Chatty Admin <chatty@example.com>'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysqliscrazyman@localhost/chatty_test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysqliscrazyman@localhost/chatty_prod'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}