from flask import Blueprint
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import views
from flask import jsonify
from flask import g

from apps.cms.models import CMSUser
from apps.cms.forms import LoginForm, ResetPwdForm
from apps.cms.decorators import login_required

from bbs.exts import db
from bbs.config import CMS_USER_ID


bp = Blueprint('cms', __name__, url_prefix='/cms/')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


class ResetPwdView(views.MethodView):

    @login_required
    def get(self, message=None):
        return render_template('cms/cms_resetpwd.html')
    
    @login_required
    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd1.data
            user = g.cms_user
            
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                data = {
                    'code': 0,
                    'message': 'OK',
                }
                return jsonify(data)
            else:
                data = {
                    'code': 1,
                    'message': '密码错误',
                }
                return jsonify(data)
        else:
            message = form.get_error()
            data = {
                'code': 2,
                'message': message
            }
            return jsonify(data)


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


bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
