# -*- coding: utf-8 -*-
from .db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, unique=True)

    create_time = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False
    )
    last_time = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.current_timestamp(),
        nullable=False
    )
    deleted = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    def delete(self, commit=True):
        self.deleted = True
        if commit:
            db.session.commit

    @classmethod
    def get_by_id(cls, id):
        return cls.filter_by(id=id).first()

    @classmethod
    def filter_by(cls, **kwargs):
        return cls.query.filter_by(deleted=False, **kwargs)
