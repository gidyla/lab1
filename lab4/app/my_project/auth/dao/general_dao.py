# my_project/auth/dao/general_dao.py

from typing import Type, Any
from sqlalchemy.orm import DeclarativeMeta

from ... import db


class GeneralDAO:
    """
    Base DAO class with common CRUD operations.
    Subclasses must define `model`.
    """

    model: Type[DeclarativeMeta] = None

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, item_id: int):
        return cls.model.query.get(item_id)

    @classmethod
    def create(cls, **kwargs) -> Any:
        obj = cls.model(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def update(cls, item_id: int, **kwargs):
        obj = cls.get_by_id(item_id)
        if not obj:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        db.session.commit()
        return obj

    @classmethod
    def delete(cls, item_id: int) -> bool:
        obj = cls.get_by_id(item_id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
