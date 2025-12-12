# my_project/auth/domain/orders/room_location.py

from .... import db
from sqlalchemy import Column, Integer, String


class RoomLocation(db.Model):
    __tablename__ = 'room_location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(String(100), nullable=False)
    floor = Column(Integer, nullable=True)

    def __init__(self, room_number: str, floor: int = None):
        self.room_number = room_number
        self.floor = floor

    def to_dict(self):
        return {
            "id": self.id,
            "room_number": self.room_number,
            "floor": self.floor
        }
