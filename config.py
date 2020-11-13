class Config:
    SECRET_KEY = 'You cannot guess me suckker'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysqliscrazyman@localhost/chatty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

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