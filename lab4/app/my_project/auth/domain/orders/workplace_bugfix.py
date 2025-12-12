# my_project/auth/domain/orders/workplace_bugfix.py

from .... import db
from sqlalchemy import Column, Integer, String, ForeignKey


class WorkplaceBugfix(db.Model):
    __tablename__ = 'workplace_bugfix'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace_id = Column(Integer, nullable=False)
    description = Column(String(1024), nullable=False)
    status = Column(String(100), nullable=True)

    def __init__(self, workplace_id: int, description: str, status: str = None):
        self.workplace_id = workplace_id
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "workplace_id": self.workplace_id,
            "description": self.description,
            "status": self.status
        }
