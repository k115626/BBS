from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo

from apps.forms import BaseFrom

class LoginForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(1, 6, message='请输入正确格式的密码(长度1-6)')])
    remember = IntegerField()


class ResetPwdForm(BaseFrom):
    oldpwd = StringField(validators=[Length(1, 6, message='请输入正确格式的旧密码(长度1-6)')])
    newpwd1 = StringField(validators=[Length(1, 6, message='请输入正确格式的新密码(长度1-6)')])
    newpwd2 = StringField(validators=[Length(1, 6, message='请再次输入正确格式的新密码(长度1-6)'), EqualTo('newpwd1', message='两次密码输入不一致')])



