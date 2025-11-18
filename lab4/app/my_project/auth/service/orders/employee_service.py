from lab4.app.my_project.auth.dao import employee_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):

    _dao = employee_dao