from flask import Flask
from bbs import config
from bbs import exts

from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp



def create_app():
    app = Flask(__name__, static_folder=config.STATIC_FOLDER, template_folder=config.TEMPLATES_FOLDER)

    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    exts.init_ext(app)

    return app


