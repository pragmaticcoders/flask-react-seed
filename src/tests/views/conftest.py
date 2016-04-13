# -*- coding: utf-8 -*-
from flask import json


def raw_call_api(client, url, method='GET', headers=None, **kwargs):
    if headers is None:
        headers = get_api_headers()

    fn = getattr(client, method.lower())

    response = fn(url, headers=headers, **kwargs)
    data = json.loads(response.data.decode())

    if response.status_code == 200:
        assert data['error'] is None
        assert data['message'] is not None

    return response, data


def call_api(client, url, headers=None, method='GET',
             payload=None):
    if method in ('POST', 'PUT'):
        payload = json.dumps(payload) if payload else None
    return raw_call_api(client, url, method, headers=headers, data=payload)


def get_api_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


def assert_notimplemented(response, data):
    assert response.status_code == 501
    assert data == {
        'error': 'notimplemented',
        'message': None,
    }
