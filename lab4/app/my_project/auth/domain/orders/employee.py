# my_project/auth/domain/orders/employee.py

from .... import db
from sqlalchemy import Column, Integer, String


class Employee(db.Model):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    position = Column(String(255), nullable=True)

    def __init__(self, first_name: str, last_name: str, position: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position
        }
