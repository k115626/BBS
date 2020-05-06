import shortuuid
import enum
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from bbs.exts import db


class GenderEnum(enum.Enum):

    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKONW = 4


class FrontUser(db.Model):

    __tablename__ = 'front_user'

    id = db.Column(db.String(128), primary_key=True, default=shortuuid.uuid)
    telephone = db.Column(db.String(16), unique=True, nullable=False)
    username = db.Column(db.String(32), nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64))
    realname = db.Column(db.String(32))
    avatar = db.Column(db.String(128))
    signature = db.Column(db.String(128))
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.UNKONW)
    join_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        if 'password' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(FrontUser, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
