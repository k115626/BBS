from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length

class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(1, 6, message='请输入正确的密码格式(长度1-6)')])
    remember = IntegerField()
