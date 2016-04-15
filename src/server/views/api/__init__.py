# -*- coding: utf-8 -*-
from flask import Blueprint


api_bp = Blueprint('api', __name__)


def init_api(app, url_prefix=''):

    from .about import About
    api_bp.add_url_rule(
        '/about',
        view_func=About.as_view('about')
    )
    # import and register views here

    app.register_blueprint(api_bp, url_prefix=url_prefix)
