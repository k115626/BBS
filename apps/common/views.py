from io import BytesIO

from flask import Blueprint, request
from flask import make_response

from .forms import SMSCaptchaForm

from utils import restful
from utils.captcha import Captcha
from utils import sendsms
from utils.bbscache import rds


bp = Blueprint('common', __name__, url_prefix='/common/')


@bp.route('/')
def index():
    return 'common index'


@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        print(captcha)
        if sendsms.send_sms(telephone, captcha):
            rds.set(telephone, captcha)
            return restful.restful_success()
        else:
            # return restful.restful_servererror('服务器错误')
            rds.set(telephone, captcha)
            return restful.restful_success()
    else:
        return restful.restful_parameserror('参数错误')


@bp.route('/captcha/')
def graph_captcha():
    text, image =Captcha.gene_graph_captcha()
    rds.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp
