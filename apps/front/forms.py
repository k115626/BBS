from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp,EqualTo,ValidationError
from utils.bbscache import rds

from .models import FrontUser


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！')])
    # sms_captcha = StringField(validators=[Regexp(r".{4}", message='请输入正确格式的短信验证码！')])
    username = StringField(validators=[Regexp(r".{2,20}", message='请输入正确格式的用户名！')])
    password1 = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo("password1", message='两次输入的密码不一致！')])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}", message='请输入正确格式的短信验证码！')])

    def validate_telephone(self, field):
        telephone = self.telephone.data
        if FrontUser.query.filter_by(telephone=telephone).first():
            raise ValidationError(message='手机号码已经注册！')

    def validate_sms_captcha(self, field):
        sms_captcha = field.data
        telephone = self.telephone.data
        sms_captcha_mem = rds.get(telephone)
        if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码错误！')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph_captcha_mem = rds.get(graph_captcha.lower())
        if not graph_captcha_mem:
            raise ValidationError(message='图形验证码错误！')


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！')])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])
    remeber = StringField()