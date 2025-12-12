# my_project/auth/domain/orders/device_type.py

from .... import db
from sqlalchemy import Column, Integer, String


class DeviceType(db.Model):
    __tablename__ = 'device_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
