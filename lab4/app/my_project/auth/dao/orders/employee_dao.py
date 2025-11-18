from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    _domain_type = Employee
