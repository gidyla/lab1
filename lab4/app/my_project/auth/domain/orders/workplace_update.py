from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WorkplaceUpdate(db.Model, IDto):

    __tablename__ = "workplace_update"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    update_service_id = db.Column(db.Integer, db.ForeignKey('update_service.id'), nullable=False)
    update_service = db.relationship('UpdateService', backref='workplace_update')
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship('Workplace', backref='workplace_update')

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.update_service_id}, {self.workplace_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "update_service_id": self.update_service_id,
            "workplace_id": self.workplace_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WorkplaceUpdate:
        obj = WorkplaceUpdate(**dto_dict)
        return obj
