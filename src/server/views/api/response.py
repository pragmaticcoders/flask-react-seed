from functools import wraps
from flask import jsonify


class ApiResponseException(Exception):

    def __init__(self, msg=None):
        if msg is not None:
            self.msg = msg

    code = 500
    msg = 'servererror'


class ApiBadrequestException(ApiResponseException):
    code = 400
    msg = 'badrequest'


class ApiUnauthorizedException(ApiResponseException):
    code = 401
    msg = 'unauthorized'


class ApiForbiddenException(ApiResponseException):
    code = 403
    msg = 'forbidden'


class ApiNotImplementedException(ApiResponseException):
    code = 501
    msg = 'notimplemented'


def _response(message, status_code=200, error_message=None):
    response = jsonify({
        'error': error_message,
        'message': message,
    })
    response.status_code = status_code
    return response


def response(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
        except ApiResponseException as ex:
            return _response(None, ex.code, ex.msg)
        return _response(result)
    return wrapper


def abort_badrequest(msg=None):
    raise ApiBadrequestException(msg=msg)


def abort_unauthorized(msg=None):
    raise ApiUnauthorizedException(msg=msg)


def abort_forbidden(msg=None):
    raise ApiForbiddenException(msg=msg)


def abort_notimplemented(msg=None):
    raise ApiNotImplementedException(msg=msg)
