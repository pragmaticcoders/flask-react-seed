# -*- coding: utf-8 -*-
from flask.views import MethodView

from .response import response, abort_notimplemented


class BaseList(MethodView):

    @response
    def get(self):
        abort_notimplemented()

    @response
    def post(self):
        abort_notimplemented()


class Base(MethodView):

    @response
    def get(self, _id):
        abort_notimplemented()

    @response
    def put(self, _id):
        abort_notimplemented()

    @response
    def delete(self, _id):
        abort_notimplemented()
