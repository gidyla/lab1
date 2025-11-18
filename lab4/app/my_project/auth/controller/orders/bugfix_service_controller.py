from lab4.app.my_project.auth.service import bugfix_service_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BugfixServiceController(GeneralController):

    _service = bugfix_service_service
