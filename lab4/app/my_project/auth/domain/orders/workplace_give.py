from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WorkplaceGive(db.Model, IDto):

    __tablename__ = "workplace_give"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    give_service_id = db.Column(db.Integer, db.ForeignKey('give_service.id'), nullable=False)
    give_service = db.relationship('GiveService', backref='workplace_give')
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship('Workplace', backref='workplace_give')

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.give_service_id}, {self.workplace_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "give_service_id": self.give_service_id,
            "workplace_id": self.workplace_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WorkplaceGive:
        obj = WorkplaceGive(**dto_dict)
        return obj
