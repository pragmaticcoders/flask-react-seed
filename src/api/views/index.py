# -*- coding: utf-8 -*-
from flask import Blueprint

index_page = Blueprint('index', __name__)


@index_page.route('/')
@index_page.route('/<path:ignored>')
def index():
    return index_page.send_static_file('index.html')
