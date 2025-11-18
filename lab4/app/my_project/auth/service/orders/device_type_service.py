from lab4.app.my_project.auth.dao import device_type_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class DeviceTypeService(GeneralService):

    _dao = device_type_dao