from my_project.auth.service import workplace_repair_service
from my_project.auth.controller.general_controller import GeneralController


class WorkplaceRepairController(GeneralController):

    _service = workplace_repair_service
