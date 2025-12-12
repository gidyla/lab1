# my_project/auth/domain/orders/workplace_exchange.py

from .... import db
from sqlalchemy import Column, Integer, String


class WorkplaceExchange(db.Model):
    __tablename__ = 'workplace_exchange'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace_id = Column(Integer, nullable=False)
    exchange_service = Column(String(255), nullable=False)
    status = Column(String(100), nullable=True)

    def __init__(self, workplace_id: int, exchange_service: str, status: str = None):
        self.workplace_id = workplace_id
        self.exchange_service = exchange_service
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "workplace_id": self.workplace_id,
            "exchange_service": self.exchange_service,
            "status": self.status
        }
