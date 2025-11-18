from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class RoomLocation(db.Model, IDto):

    __tablename__ = "room_location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    room = db.Column(db.String(45), nullable=False)
    desk = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, '{self.room}', '{self.desk}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "room": self.room,
            "desk": self.desk
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RoomLocation:
        obj = RoomLocation(**dto_dict)
        return obj
