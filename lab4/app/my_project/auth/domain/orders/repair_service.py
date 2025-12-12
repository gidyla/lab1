# my_project/auth/domain/orders/repair_service.py

from .... import db
from sqlalchemy import Column, Integer, String


class RepairService(db.Model):
    __tablename__ = 'repair_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
