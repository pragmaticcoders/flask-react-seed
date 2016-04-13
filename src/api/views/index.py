# -*- coding: utf-8 -*-
import os

from flask import Blueprint, send_from_directory
from config import SRC_ROOT


STATIC_DIR = os.path.join(SRC_ROOT, 'app', 'dist')


index_page = Blueprint('index', __name__)
_index_html = None


@index_page.route('/static/<path:filename>')
def static(filename):
    return send_from_directory(
        STATIC_DIR,
        filename, as_attachment=True)


@index_page.route('/')
@index_page.route('/<path:ignored>')
def index(ignored=None):
    global _index_html
    if _index_html is None:
        with open(os.path.join(SRC_ROOT, 'app', 'index.html')) as index_html:
            _index_html = index_html.read()
    return _index_html
