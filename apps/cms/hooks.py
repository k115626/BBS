from flask import session
from flask import g

from .views import bp
from .models import CMSUser

from bbs.config import CMS_USER_ID


@bp.before_request
def before_request():
    if CMS_USER_ID in session:
        uid = session.get(CMS_USER_ID)
        user = CMSUser.query.get(uid)
        if user:
            g.cms_user = user