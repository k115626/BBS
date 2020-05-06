from flask import Blueprint, request

from .forms import SMSCaptchaForm

from utils import restful
from utils.captcha import Captcha
from utils import sendsms


bp = Blueprint('commmon', __name__, url_prefix='/common/')

@bp.route('/')
def index():
    return 'common index'


@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        if sendsms.send_sms(telephone, captcha):
            return restful.restful_success()
        else:
            return restful.restful_servererror('服务器错误')
    else:
        return restful.restful_parameserror('参数错误')
