from lab4.app.my_project.auth.dao import bugfix_service_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BugfixServiceService(GeneralService):

    _dao = bugfix_service_dao