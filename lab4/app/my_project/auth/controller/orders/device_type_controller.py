from my_project.auth.service import device_type_service
from my_project.auth.controller.general_controller import GeneralController


class DeviceTypeController(GeneralController):

    _service = device_type_service