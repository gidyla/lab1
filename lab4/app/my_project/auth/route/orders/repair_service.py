from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import repair_service_controller
from my_project.auth.domain import RepairService

repair_service_bp = Blueprint('RepairService', __name__, url_prefix='/repair-service')


@repair_service_bp.get('')
def get_all_repair_service() -> Response:
    """
    Get all repair services
    ---
    tags:
      - RepairService
    responses:
      200:
        description: List of all repair services
    """
    return make_response(jsonify(repair_service_controller.find_all()), HTTPStatus.OK)


@repair_service_bp.post('')
def create_repair_service() -> Response:
    """
    Create new repair service
    ---
    tags:
      - RepairService
    parameters:
      - in: body
        name: repair_service
        required: true
        description: Repair service data
        schema:
          type: object
          properties:
            device_id:
              type: integer
              description: Device under repair
            employee_id:
              type: integer
              description: Assigned technician
            repair_status:
              type: string
              description: Status of repair
            description:
              type: string
              description: Problem description
    responses:
      201:
        description: Repair service created successfully
    """
    content = request.get_json()
    repair_service = RepairService.create_from_dto(content)
    repair_service_controller.create(repair_service)
    return make_response(jsonify(repair_service.put_into_dto()), HTTPStatus.CREATED)


@repair_service_bp.get('/<int:repair_service_id>')
def get_repair_service(repair_service_id: int) -> Response:
    """
    Get repair service by ID
    ---
    tags:
      - RepairService
    parameters:
      - in: path
        name: repair_service_id
        type: integer
        required: true
        description: Repair service ID
    responses:
      200:
        description: Repair service data
      404:
        description: Repair service not found
    """
    return make_response(jsonify(repair_service_controller.find_by_id(repair_service_id)), HTTPStatus.OK)


@repair_service_bp.put('/<int:repair_service_id>')
def update_repair_service(repair_service_id: int) -> Response:
    """
    Update repair service
    ---
    tags:
      - RepairService
    parameters:
      - in: path
        name: repair_service_id
        type: integer
        required: true
        description: Repair service ID
      - in: body
        name: repair_service
        required: true
        description: Updated repair service data
        schema:
          type: object
          properties:
            device_id:
              type: integer
            employee_id:
              type: integer
            repair_status:
              type: string
            description:
              type: string
    responses:
      200:
        description: Repair service updated successfully
      404:
        description: Repair service not found
    """
    content = request.get_json()
    repair_service = RepairService.create_from_dto(content)
    repair_service_controller.update(repair_service_id, repair_service)
    return make_response("RepairService updated", HTTPStatus.OK)


@repair_service_bp.patch('/<int:repair_service_id>')
def patch_repair_service(repair_service_id: int) -> Response:
    """
    Partially update repair service
    ---
    tags:
      - RepairService
    parameters:
      - in: path
        name: repair_service_id
        type: integer
        required: true
        description: Repair service ID
      - in: body
        name: repair_service
        description: Partial repair service data
        required: true
        schema:
          type: object
          properties:
            device_id:
              type: integer
            employee_id:
              type: integer
            repair_status:
              type: string
            description:
              type: string
    responses:
      200:
        description: Repair service updated successfully
      404:
        description: Repair service not found
    """
    content = request.get_json()
    repair_service_controller.patch(repair_service_id, content)
    return make_response("RepairService updated", HTTPStatus.OK)


@repair_service_bp.delete('/<int:repair_service_id>')
def delete_repair_service(repair_service_id: int) -> Response:
    """
    Delete repair service
    ---
    tags:
      - RepairService
    parameters:
      - in: path
        name: repair_service_id
        type: integer
        required: true
        description: Repair service ID
    responses:
      200:
        description: Repair service deleted successfully
      404:
        description: Repair service not found
    """
    repair_service_controller.delete(repair_service_id)
    return make_response("RepairService deleted", HTTPStatus.OK)
