from flask import Blueprint
from apps.cms.models import CMSUser
from bbs.exts import db

bp = Blueprint('cms', __name__, url_prefix='/cms/')

@bp.route('/')
def index():
    return 'cms index'


@bp.route('/create_user/')
def create_user():
    user = CMSUser('guest', '123', 'guest@163.com')
    # user.username = 'guest'
    # user.password = '123'
    # user.email = 'guest@163.com'
    db.session.add(user)
    db.session.commit()
    return 'add user success'


