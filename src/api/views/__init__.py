# -*- coding: utf-8 -*-


def init_views(app, db):

    from .api import init_api
    init_api(app, url_prefix='/api')

    from .index import index_page
    app.register_blueprint(index_page)
