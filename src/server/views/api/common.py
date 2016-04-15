from flask import request

from .response import abort_badrequest


def request_get_json(schema, **kwargs):
    json_data = request.get_json()
    if not json_data:
        abort_badrequest('No input data provided')

    data, errors = schema.load(json_data, **kwargs)

    if errors:
        return abort_badrequest(errors)

    return data
