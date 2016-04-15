# -*- coding: utf-8 -*-

import os
import sys
import pytest

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(TESTS_ROOT)

sys.path.append(SRC_ROOT)

from server import create_app


app = create_app(
    config_object='config.DevelopmentTesting'
)


@pytest.yield_fixture()
def db():
    with app.app_context():
        from app.db import db
        db.session.close()
        db.drop_all()
        db.create_all()
        yield db


@pytest.yield_fixture()
def client(db):
    client = app.test_client()
    client.testing = True
    yield client


@pytest.fixture()
def get_resurce_path():
    return lambda p: os.path.join(TESTS_ROOT, 'resurces', p)
