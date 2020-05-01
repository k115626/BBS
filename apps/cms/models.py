from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from bbs.exts import db


class CMSUser(db.Model):
    __tablename__ = 'cms_user'

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=True)
    _password = db.Column(db.String(256), nullable=True)
    email = db.Column(db.String(64), nullable=True, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
