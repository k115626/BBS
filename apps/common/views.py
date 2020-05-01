from flask import Blueprint

bp = Blueprint('commmon', __name__, url_prefix='/common/')

@bp.route('/')
def index():
    return 'common index'

