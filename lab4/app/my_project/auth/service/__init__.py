from .orders.bugfix_service_service import BugfixServiceService
from .orders.device_type_service import DeviceTypeService
from .orders.employee_service import EmployeeService
from .orders.exchange_service_service   import ExchangeServiceService
from .orders.give_service_service import GiveServiceService
from .orders.office_location_service import OfficeLocationService
from .orders.repair_service_service import RepairServiceService
from .orders.room_location_service import RoomLocationService
from .orders.update_service_service import UpdateServiceService
from .orders.workplace_bugfix_service import WorkplaceBugfixService
from .orders.workplace_exchange_service import WorkplaceExchangeService
from .orders.workplace_give_service import WorkplaceGiveService
from .orders.workplace_repair_service import WorkplaceRepairService
from .orders.workplace_update_service import WorkplaceUpdateService
from .orders.workplace_service import WorkplaceService

bugfix_service_service = BugfixServiceService()
device_type_service = DeviceTypeService()
employee_service = EmployeeService()
exchange_service_service = ExchangeServiceService()
give_service_service = GiveServiceService()
office_location_service = OfficeLocationService()
repair_service_service = RepairServiceService()
room_location_service = RoomLocationService()
update_service_service = UpdateServiceService()
workplace_bugfix_service = WorkplaceBugfixService()
workplace_exchange_service = WorkplaceExchangeService()
workplace_give_service = WorkplaceGiveService()
workplace_repair_service = WorkplaceRepairService()
workplace_update_service = WorkplaceUpdateService()
workplace_service = WorkplaceService()
