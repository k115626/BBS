import string
import random

from flask import Blueprint
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import views
from flask import jsonify
from flask import g
from flask_mail import Message

from apps.cms.models import CMSUser, CMSPersmission
from apps.cms.forms import LoginForm, ResetPwdForm, ResetEmailForm
from apps.cms.decorators import login_required, premission_required

from bbs.exts import db
from bbs.exts import mail
from bbs.config import CMS_USER_ID

from utils import restful
from utils import bbscache


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
                return restful.restful_success()
            else:
                return restful.restful_parameserror('旧密码错误')
        else:
            return restful.restful_parameserror(form.get_error())


@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.restful_parameserror('请传递邮箱参数')
    source = list(string.ascii_letters)
    source.extend([str(x) for x in range(10)])
    captcha = ''.join(random.sample(source, 6))
    
    title = 'BBS 邮箱验证码'
    content = '您的验证码是 %s' % captcha
    message = Message(subject=title, recipients=[email], body=content)
    try:
        bbscache.set(email, captcha)
        mail.send(message)
        return restful.restful_success()
    except:
        return restful.restful_servererror('发送邮件服务错误')
    

class ResetEmailViews(views.MethodView):

    decorators = [login_required]  # 指定装饰器验证是否登陆用户

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            g.cms_user.email = form.email.data
            db.session.commit()
            return restful.restful_success()
        else:
            return restful.restful_parameserror(form.get_error())


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


@bp.route('/posts/')
@login_required
@premission_required(CMSPersmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_required
@premission_required(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@premission_required(CMSPersmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_required
@premission_required(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@premission_required(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@premission_required(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailViews.as_view('resetemail'))
