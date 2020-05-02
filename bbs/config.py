
import os

DEBUG = True

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
TEMPLATES_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'bbs'

DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USERNAME, DB_PASSWORD,
            DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'sdfg12GJK.okj&*('

CMS_USER_ID = 'cms_asgadfhdfdsh'
