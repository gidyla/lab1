# my_project/auth/domain/orders/workplace_repair.py

from .... import db
from sqlalchemy import Column, Integer, String


class WorkplaceRepair(db.Model):
    __tablename__ = 'workplace_repair'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace_id = Column(Integer, nullable=False)
    repair_service = Column(String(255), nullable=False)
    status = Column(String(100), nullable=True)

    def __init__(self, workplace_id: int, repair_service: str, status: str = None):
        self.workplace_id = workplace_id
        self.repair_service = repair_service
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "workplace_id": self.workplace_id,
            "repair_service": self.repair_service,
            "status": self.status
        }
