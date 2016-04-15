from marshmallow import Schema, fields


class BaseSchema(Schema):

    id = fields.Int(required=True, dump_ony=True)
    create_time = fields.DateTime(required=True, dump_ony=True)
    last_time = fields.DateTime(required=True, dump_ony=True)
    deleted = fields.Boolean(required=True, dump_ony=True)
