from my_project.auth.service import workplace_bugfix_service
from my_project.auth.controller.general_controller import GeneralController


class WorkplaceBugfixController(GeneralController):

    _service = workplace_bugfix_service
