from my_project.auth.service import workplace_give_service
from my_project.auth.controller.general_controller import GeneralController


class WorkplaceGiveController(GeneralController):

    _service = workplace_give_service
