import requests
from bbs.config import YZX_SMS_PARAM, YZX_SMS_URL
from .captcha import Captcha


def send_sms(telephone, captcha):
    headers = {
        'Content-Type': 'application/json'
    }
    url = YZX_SMS_URL
    parame = YZX_SMS_PARAM.copy()
    parame['mobile'] = telephone
    parame['param'] = '{},60'.format(captcha)
    resp = requests.post(url, parame, headers=headers)
    print(resp.json())
    # try:
    #     if resp.json().code == 200:
    #         return True
    # except:
    #     return False
