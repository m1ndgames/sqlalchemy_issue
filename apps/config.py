import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASK_APP = "run.py"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI", "sqlite:///" + os.path.join(basedir, "test.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"


class DebugConfig(Config):
    DEBUG = True
    FLASK_DEBUG = 1
    ENV = "development"


# Load all possible configurations
config_dict = {"Production": ProductionConfig, "Debug": DebugConfig}
