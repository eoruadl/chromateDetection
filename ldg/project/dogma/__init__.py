from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
from datetime import timedelta

db = SQLAlchemy()
migrate = Migrate()

def create_app():   # app 실행 함수
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, auth_views, oauth_views, submit_views, detail_views
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(submit_views.bp)
    app.register_blueprint(oauth_views.bp)
    app.register_blueprint(detail_views.bp)

    return app