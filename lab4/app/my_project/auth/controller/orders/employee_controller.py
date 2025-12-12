from my_project.auth.service import employee_service
from my_project.auth.controller.general_controller import GeneralController


class EmployeeController(GeneralController):

    _service = employee_service