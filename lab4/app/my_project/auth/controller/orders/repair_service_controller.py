from lab4.app.my_project.auth.service import repair_service_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RepairServiceController(GeneralController):

    _service = repair_service_service