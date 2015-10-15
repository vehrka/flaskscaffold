import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_VAR = 'DEV_DATABASE_URL'


class TestingConfig(Config):
    TESTING = True
    DATABASE_VAR = 'TEST_DATABASE_URL'


class ProductionConfig(Config):
    DATABASE_VAR = 'DATABASE_URL'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
