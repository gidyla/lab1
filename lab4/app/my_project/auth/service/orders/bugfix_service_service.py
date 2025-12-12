# my_project/auth/service/orders/bugfix_service_service.py

from ...dao import bugfix_service_dao


class BugfixServiceService:

    @staticmethod
    def get_all():
        return bugfix_service_dao.get_all()

    @staticmethod
    def get_by_id(item_id: int):
        return bugfix_service_dao.get_by_id(item_id)

    @staticmethod
    def create(data: dict):
        return bugfix_service_dao.create(data)

    @staticmethod
    def update(item_id: int, data: dict):
        return bugfix_service_dao.update(item_id, data)

    @staticmethod
    def delete(item_id: int):
        return bugfix_service_dao.delete(item_id)
