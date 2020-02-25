from redis import StrictRedis
class Config(object):
    DEBUG = True
    pass
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:123456@127.0.0.1:3306/daita?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    REDIS_HOST, REDIS_PORT, REDIS_DB = "127.0.0.1", 6379, 5
    # base64.b64encode(os.urandom(48)).decode()
    SECRET_KEY = 'wMjFBDZtATCGqLwN1W2PLd/d5gSkB1qPFagWQ7FKQr2Z842SyD1rfv6Z8ENE6Q6o'
    SESSION_TYPE = "redis"  # session 存入到 redis中
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    PERMANENT_SESSION_LIFETIME = 24*60*60*30

    JSON_AS_ASCII = False







