import os


class Config(object):
    HOST = str(os.environ.get("DB_HOST", "localhost"))
    DATABASE = str(os.environ.get("DB_DATABASE", "zusammenioctest"))
    USERNAME = str(os.environ.get("DB_USERNAME", "root"))
    PASSWORD = str(os.environ.get("DB_PASSWORD", "tatapjang"))

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + \
        ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
