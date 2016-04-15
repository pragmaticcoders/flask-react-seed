from tests.views.conftest import call_api, assert_notimplemented


def test_about_get(client):
    response, data = call_api(client, '/api/about')
    assert data['message'] == {'version': '0.0.1'}


def test_about_post(client):
    response, data = call_api(client, '/api/about', method='POST')
    assert_notimplemented(response, data)
