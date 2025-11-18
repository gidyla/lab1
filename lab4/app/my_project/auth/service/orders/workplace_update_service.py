from lab4.app.my_project.auth.dao import workplace_update_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceUpdateService(GeneralService):

    _dao = workplace_update_dao