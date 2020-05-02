from flask import Blueprint
from flask import session
from flask import redirect, url_for
from apps.cms.models import CMSUser
from apps.cms.forms import LoginForm
from bbs.exts import db
from apps.cms.decorators import login_required

from flask import render_template
from flask import request
from bbs.config import CMS_USER_ID


bp = Blueprint('cms', __name__, url_prefix='/cms/')


@bp.route('/')
@login_required
def index():
    return 'cms index'
    

@bp.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('cms/cms_login.html')
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[CMS_USER_ID] = user.uid
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return render_template('cms/cms_login.html', message='邮箱或者密码错误')
        else:
            message = form.errors.popitem()[1][0]
            return render_template('cms/cms_login.html', message=message)

