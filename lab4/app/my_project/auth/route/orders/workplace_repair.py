from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import workplace_repair_controller
from my_project.auth.domain import WorkplaceRepair

workplace_repair_bp = Blueprint('WorkplaceRepair', __name__, url_prefix='/workplace-repair')


@workplace_repair_bp.get('')
def get_all_workplace_repair() -> Response:
    """
    Get all workplace repair records
    ---
    tags:
      - WorkplaceRepair
    responses:
      200:
        description: List of all workplace repair records
    """
    return make_response(jsonify(workplace_repair_controller.find_all()), HTTPStatus.OK)


@workplace_repair_bp.post('')
def create_workplace_repair() -> Response:
    """
    Create new workplace repair record
    ---
    tags:
      - WorkplaceRepair
    parameters:
      - in: body
        name: workplace_repair
        required: true
        description: Workplace repair record data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
              description: Workplace ID
            repair_service_id:
              type: integer
              description: Repair service ID
            description:
              type: string
              description: Repair details
    responses:
      201:
        description: Workplace repair created successfully
    """
    content = request.get_json()
    workplace_repair = WorkplaceRepair.create_from_dto(content)
    workplace_repair_controller.create(workplace_repair)
    return make_response(jsonify(workplace_repair.put_into_dto()), HTTPStatus.CREATED)


@workplace_repair_bp.get('/<int:workplace_repair_id>')
def get_workplace_repair(workplace_repair_id: int) -> Response:
    """
    Get workplace repair record by ID
    ---
    tags:
      - WorkplaceRepair
    parameters:
      - in: path
        name: workplace_repair_id
        type: integer
        required: true
        description: Workplace repair ID
    responses:
      200:
        description: Workplace repair record
      404:
        description: Record not found
    """
    return make_response(jsonify(workplace_repair_controller.find_by_id(workplace_repair_id)), HTTPStatus.OK)


@workplace_repair_bp.put('/<int:workplace_repair_id>')
def update_workplace_repair(workplace_repair_id: int) -> Response:
    """
    Update workplace repair record
    ---
    tags:
      - WorkplaceRepair
    parameters:
      - in: path
        name: workplace_repair_id
        required: true
        type: integer
        description: Workplace repair ID
      - in: body
        name: workplace_repair
        required: true
        description: Updated workplace repair data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            repair_service_id:
              type: integer
            description:
              type: string
    responses:
      200:
        description: Workplace repair updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_repair = WorkplaceRepair.create_from_dto(content)
    workplace_repair_controller.repair(workplace_repair_id, workplace_repair)
    return make_response("WorkplaceRepair updated", HTTPStatus.OK)


@workplace_repair_bp.patch('/<int:workplace_repair_id>')
def patch_workplace_repair(workplace_repair_id: int) -> Response:
    """
    Partially update workplace repair record
    ---
    tags:
      - WorkplaceRepair
    parameters:
      - in: path
        name: workplace_repair_id
        required: true
        type: integer
        description: Workplace repair ID
      - in: body
        name: workplace_repair
        required: true
        description: Partial repair update data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            repair_service_id:
              type: integer
            description:
              type: string
    responses:
      200:
        description: Workplace repair updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_repair_controller.patch(workplace_repair_id, content)
    return make_response("WorkplaceRepair updated", HTTPStatus.OK)


@workplace_repair_bp.delete('/<int:workplace_repair_id>')
def delete_workplace_repair(workplace_repair_id: int) -> Response:
    """
    Delete workplace repair record
    ---
    tags:
      - WorkplaceRepair
    parameters:
      - in: path
        name: workplace_repair_id
        required: true
        type: integer
        description: Workplace repair ID
    responses:
      200:
        description: Workplace repair deleted successfully
      404:
        description: Record not found
    """
    workplace_repair_controller.delete(workplace_repair_id)
    return make_response("WorkplaceRepair deleted", HTTPStatus.OK)
