# -*- coding: utf-8 -*-

import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import SRC_ROOT


db = SQLAlchemy()

def db_data_seed():
    pass


def init_db(app):
    db.init_app(app)
    from .models import BaseModel

    migrate = Migrate(
        app, db,
        directory=os.path.join(SRC_ROOT, 'migrations')
    )

    @app.before_first_request
    def setup_database(*args, **kwargs):
        db_data_seed()

    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.session.rollback()
            db.session.remove()
        db.session.remove()

    return db
