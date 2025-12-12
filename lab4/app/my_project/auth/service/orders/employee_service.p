# my_project/auth/service/orders/employee_service.py

from ...dao import employee_dao


class EmployeeService:

    @staticmethod
    def get_all():
        return employee_dao.get_all()

    @staticmethod
    def get_by_id(item_id: int):
        return employee_dao.get_by_id(item_id)

    @staticmethod
    def create(data: dict):
        return employee_dao.create(data)

    @staticmethod
    def update(item_id: int, data: dict):
        return employee_dao.update(item_id, data)

    @staticmethod
    def delete(item_id: int):
        return employee_dao.delete(item_id)
