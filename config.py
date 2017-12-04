class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:////tmp/document.db'
    METADATA_URL = "http://127.0.0.1:5000/metadata"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
