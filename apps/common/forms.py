from hashlib import md5

from apps.forms import BaseFrom
from wtforms import StringField
from wtforms.validators import regexp, InputRequired


class SMSCaptchaForm(BaseFrom):
    salt = 'stsdh@*567VGH%^&HJM'
    telephone = StringField(validators=[regexp(r'^1[345789]\d{9}$')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data
        sign2 = md5((telephone+timestamp+self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False