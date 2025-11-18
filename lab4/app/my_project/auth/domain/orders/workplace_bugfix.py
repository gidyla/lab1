from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WorkplaceBugfix(db.Model, IDto):

    __tablename__ = "workplace_bugfix"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    bugfix_service_id = db.Column(db.Integer, db.ForeignKey('bugfix_service.id'), nullable=False)
    bugfix_service = db.relationship('BugfixService', backref='workplace_bugfix')
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship('Workplace', backref='WorkplaceBugfix')

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.bugfix_service_id}, {self.workplace_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "bugfix_service_id": self.bugfix_service_id,
            "workplace_id": self.workplace_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WorkplaceBugfix:
        obj = WorkplaceBugfix(**dto_dict)
        return obj
