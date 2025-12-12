# my_project/auth/service/orders/device_type_service.py

from ...dao import device_type_dao


class DeviceTypeService:

    @staticmethod
    def get_all():
        return device_type_dao.get_all()

    @staticmethod
    def get_by_id(item_id: int):
        return device_type_dao.get_by_id(item_id)

    @staticmethod
    def create(data: dict):
        return device_type_dao.create(data)

    @staticmethod
    def update(item_id: int, data: dict):
        return device_type_dao.update(item_id, data)

    @staticmethod
    def delete(item_id: int):
        return device_type_dao.delete(item_id)
