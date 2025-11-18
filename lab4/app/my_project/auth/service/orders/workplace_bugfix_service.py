from lab4.app.my_project.auth.dao import workplace_bugfix_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceBugfixService(GeneralService):

    _dao = workplace_bugfix_dao