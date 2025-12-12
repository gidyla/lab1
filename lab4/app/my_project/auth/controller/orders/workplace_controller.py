from typing import List

from my_project.auth.service import workplace_service
from my_project.auth.controller.general_controller import GeneralController


class WorkplaceController(GeneralController):

    _service = workplace_service

    def get_employee_by_office(self, office_location_id: int) -> List[object]:
        return self._service.get_employee_by_office(office_location_id)

    def get_office_by_employee(self, employee_id: int) -> List[object]:
        return self._service.get_office_by_employee(employee_id)
