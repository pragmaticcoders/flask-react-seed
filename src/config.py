# -*- coding: utf-8 -*-

import os


SRC_ROOT = os.path.abspath(os.path.dirname(__file__))


class _Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '36G4DnIKqX7uyNWNiqB0bSBn8QSQVd9V'
    DATABASE_URI = 'postgresql://postgres@localhost:5432/postgres'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(_Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    DEBUG = True


class Development(_Config):
    DEBUG = True


class DevelopmentTesting(Development):
    DATABASE_URI = 'postgresql://postgres@localhost:5433/postgres'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    TESTING = True


class ProductionTesting(Production):
    TESTING = True
