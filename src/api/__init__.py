# -*- coding: utf-8 -*-

import os

from flask import Flask


APP_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(APP_ROOT)


def create_app(config_object):
    app = Flask(__name__, static_folder=os.path.join(
        SRC_ROOT, 'app', 'dist'
    ))
    app.config.from_object(config_object)

    with app.app_context():

        from .db import init_db
        db = init_db(app)

        from .views import init_views
        init_views(app, db)

    return app
