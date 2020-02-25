import pymongo
from flask import Flask
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from application.settings.dev import DevelopmentConfig
from application.settings.prop import ProductionConfig

print("AAAAAAAAAAAAAAAA")
config = {
    "dev": DevelopmentConfig,
    "prop": ProductionConfig,
}

redis_store = None
db = SQLAlchemy()
csrf = CSRFProtect()
mgo = pymongo.MongoClient()
def init_app(config_name):
    global redis_store

    app = Flask(__name__)

    Config = config[config_name]

    app.config.from_object(Config)

    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB-1)

    csrf.init_app(app)

    Session(app)

    db.init_app(app)

    from .modules.index import index
    app.register_blueprint(index, url_prefix='')



    return app