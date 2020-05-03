from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from wtforms import ValidationError

from flask import g

from apps.forms import BaseFrom

from utils import bbscache

class LoginForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(1, 6, message='请输入正确格式的密码(长度1-6)')])
    remember = IntegerField()


class ResetPwdForm(BaseFrom):
    oldpwd = StringField(validators=[Length(1, 6, message='请输入正确格式的旧密码(长度1-6)')])
    newpwd1 = StringField(validators=[Length(1, 6, message='请输入正确格式的新密码(长度1-6)')])
    newpwd2 = StringField(validators=[Length(1, 6, message='请再次输入正确格式的新密码(长度1-6)'), EqualTo('newpwd1', message='两次密码输入不一致')])


class ResetEmailForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱!')])
    captcha = StringField(validators=[Length(6, 6, message='请输入正确的验证码!')])

    def validate_captcha(self, filed):
        if not bbscache.get(self.email.data):
            raise ValidationError('邮箱验证码已失效!')
        if bbscache.get(self.email.data).lower() != filed.data.lower():
            raise ValidationError('邮箱验证码错误!')

    def validate_email(self, filed):
        if g.cms_user.email == filed.data:
            raise ValidationError('不能修改为相同的邮箱!')



