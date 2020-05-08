from flask import (
    Blueprint,
    views,
    render_template,
    request,
    )

from bbs.exts import db
from .forms import SignupForm
from .models import FrontUser
from utils import restful, safeurl

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'front index'


class SignupView(views.MethodView):

    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeurl.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        else:
            return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = FrontUser(telephone=telephone, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return restful.restful_success()
        else:
            return restful.restful_parameserror(message=form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))