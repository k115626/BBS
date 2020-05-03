# coding: utf-8
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()  
migrate = Migrate()  
mail = Mail()


def init_ext(app):
    db.init_app(app)  
    migrate.init_app(app, db)
    mail.init_app(app)
