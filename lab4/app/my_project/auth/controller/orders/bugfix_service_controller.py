# my_project/auth/controller/orders/bugfix_service_controller.py

from ...service import bugfix_service_service


class BugfixServiceController:

    @staticmethod
    def get_all():
        return bugfix_service_service.get_all()

    @staticmethod
    def get_by_id(item_id: int):
        return bugfix_service_service.get_by_id(item_id)

    @staticmethod
    def create(data: dict):
        return bugfix_service_service.create(data)

    @staticmethod
    def update(item_id: int, data: dict):
        return bugfix_service_service.update(item_id, data)

    @staticmethod
    def delete(item_id: int):
        return bugfix_service_service.delete(item_id)
