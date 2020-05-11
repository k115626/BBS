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
FRONT_USER_ID = 'front_sdfggfghgt'


# redis 配置
REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 1,
}


# 发送者邮箱的服务配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'chai_jk@163.com'
MAIL_PASSWORD = 'LRYSHPXGQSWCDJMF'
MAIL_DEFAULT_SENDER = 'chai_jk@163.com'
MAIL_DEBUG = False


# 云之讯发送短信验证码
YZX_SMS_URL = "https://open.ucpaas.com/ol/sms/sendsms"
YZX_SMS_PARAM ={
    "sid": "86292e777ac419a4f8032ae0d3e6d21b",
    "token": "fe026d0592a61436aa8bc5556d33f99e",
    "appid": "891294e64b4f486da68b28792093cc9a",
    "templateid": "542499",
    "param": "",
    "mobile": "",
}
