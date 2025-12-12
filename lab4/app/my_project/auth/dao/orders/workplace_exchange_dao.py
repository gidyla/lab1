# my_project/auth/dao/orders/workplace_exchange_dao.py

from ..general_dao import GeneralDAO
from .... import db
from ...domain.orders.workplace_exchange import WorkplaceExchange


class WorkplaceExchangeDAO(GeneralDAO):
    model = WorkplaceExchange

    @classmethod
    def get_all(cls):
        return [item.to_dict() for item in cls.model.query.all()]

    @classmethod
    def get_by_id(cls, item_id: int):
        item = cls.model.query.get(item_id)
        return item.to_dict() if item else None

    @classmethod
    def create(cls, data: dict):
        item = cls.model(**data)
        db.session.add(item)
        db.session.commit()
        return item.to_dict()

    @classmethod
    def update(cls, item_id: int, data: dict):
        item = cls.model.query.get(item_id)
        if not item:
            return None
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item.to_dict()

    @classmethod
    def delete(cls, item_id: int):
        item = cls.model.query.get(item_id)
        if not item:
            return False
        db.session.delete(item)
        db.session.commit()
        return True
