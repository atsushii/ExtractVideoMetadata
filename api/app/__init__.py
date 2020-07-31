from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.config import DevelopmentConfig, TestConfig
import os
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    comfig_name = os.environ.get('FLASK_ENV')

    # test environment
    if comfig_name == "test":

        db = SQLAlchemy()

        from app.views.views import api
        from app.models.models import db
        app.register_blueprint(api)

        app.config.from_object(TestConfig)
        db.init_app(app)
        app.app_context().push()

        return app

    # development environment
    from app.views.views import api
    from app.models.models import db
    app.register_blueprint(api)

    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    Migrate(app, db)

    return app
