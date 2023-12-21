import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get('DB_HOST'))
    DATABASE = str(os.environ.get('DB_DATABASE'))
    USER = str(os.environ.get('DB_USER'))
    PASSWORD = str(os.environ.get('DB_PASS'))

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
