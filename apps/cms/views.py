from flask import Blueprint
from flask import session
from apps.cms.models import CMSUser
from apps.cms.forms import LoginForm
from bbs.exts import db

from flask import render_template
from flask import request

bp = Blueprint('cms', __name__, url_prefix='/cms/')

@bp.route('/')
def index():
    return 'cms index'

@bp.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('cms/cms_login.html')
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if forms.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.fifter_by(email=email).first()
            if user and user.check_password(password):
                session['uid'] = user.id
                if remember:
                    pass
        else:
            print(form.errors)
            return self.get()

