# my_project/auth/domain/orders/bugfix_service.py

from .... import db
from sqlalchemy import Column, Integer, String


class BugfixService(db.Model):
    __tablename__ = 'bugfix_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)

    def __init__(self, title: str, description: str = None):
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
