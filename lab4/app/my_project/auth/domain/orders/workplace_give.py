# my_project/auth/domain/orders/workplace_give.py

from .... import db
from sqlalchemy import Column, Integer, String


class WorkplaceGive(db.Model):
    __tablename__ = 'workplace_give'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace_id = Column(Integer, nullable=False)
    give_service = Column(String(255), nullable=False)
    status = Column(String(100), nullable=True)

    def __init__(self, workplace_id: int, give_service: str, status: str = None):
        self.workplace_id = workplace_id
        self.give_service = give_service
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "workplace_id": self.workplace_id,
            "give_service": self.give_service,
            "status": self.status
        }
