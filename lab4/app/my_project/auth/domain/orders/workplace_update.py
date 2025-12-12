# my_project/auth/domain/orders/workplace_update.py

from .... import db
from sqlalchemy import Column, Integer, String


class WorkplaceUpdate(db.Model):
    __tablename__ = 'workplace_update'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace_id = Column(Integer, nullable=False)
    update_service = Column(String(255), nullable=False)
    status = Column(String(100), nullable=True)

    def __init__(self, workplace_id: int, update_service: str, status: str = None):
        self.workplace_id = workplace_id
        self.update_service = update_service
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "workplace_id": self.workplace_id,
            "update_service": self.update_service,
            "status": self.status
        }
