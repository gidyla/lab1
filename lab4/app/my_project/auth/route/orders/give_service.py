from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import give_service_controller
from lab4.app.my_project.auth.domain import GiveService

give_service_bp = Blueprint('GiveService', __name__, url_prefix='/give-service')


@give_service_bp.get('')
def get_all_give_service() -> Response:
    """
    Get all give services
    ---
    tags:
      - GiveService
    responses:
      200:
        description: List of all give services
    """
    return make_response(jsonify(give_service_controller.find_all()), HTTPStatus.OK)


@give_service_bp.post('')
def create_give_service() -> Response:
    """
    Create new give service
    ---
    tags:
      - GiveService
    parameters:
      - in: body
        name: give_service
        description: Give service data
        required: true
        schema:
          type: object
          properties:
            employee_id:
              type: integer
              description: Employee who gives the device
            device_id:
              type: integer
              description: Device being given out
            date_given:
              type: string
              description: Date when device was given
    responses:
      201:
        description: Give service created successfully
    """
    content = request.get_json()
    give_service = GiveService.create_from_dto(content)
    give_service_controller.create(give_service)
    return make_response(jsonify(give_service.put_into_dto()), HTTPStatus.CREATED)


@give_service_bp.get('/<int:give_service_id>')
def get_give_service(give_service_id: int) -> Response:
    """
    Get give service by ID
    ---
    tags:
      - GiveService
    parameters:
      - in: path
        name: give_service_id
        required: true
        type: integer
        description: Give service ID
    responses:
      200:
        description: Give service data
      404:
        description: Give service not found
    """
    return make_response(jsonify(give_service_controller.find_by_id(give_service_id)), HTTPStatus.OK)


@give_service_bp.put('/<int:give_service_id>')
def update_give_service(give_service_id: int) -> Response:
    """
    Update give service by ID
    ---
    tags:
      - GiveService
    parameters:
      - in: path
        name: give_service_id
        type: integer
        required: true
        description: Give service ID
      - in: body
        name: give_service
        required: true
        description: Updated give service data
        schema:
          type: object
          properties:
            employee_id:
              type: integer
            device_id:
              type: integer
            date_given:
              type: string
    responses:
      200:
        description: Give service updated successfully
      404:
        description: Give service not found
    """
    content = request.get_json()
    give_service = GiveService.create_from_dto(content)
    give_service_controller.update(give_service_id, give_service)
    return make_response("GiveService updated", HTTPStatus.OK)


@give_service_bp.patch('/<int:give_service_id>')
def patch_give_service(give_service_id: int) -> Response:
    """
    Partially update give service
    ---
    tags:
      - GiveService
    parameters:
      - in: path
        name: give_service_id
        required: true
        type: integer
        description: Give service ID
      - in: body
        name: give_service
        description: Partial give service data
        required: true
        schema:
          type: object
          properties:
            employee_id:
              type: integer
            device_id:
              type: integer
            date_given:
              type: string
    responses:
      200:
        description: Give service updated successfully
      404:
        description: Give service not found
    """
    content = request.get_json()
    give_service_controller.patch(give_service_id, content)
    return make_response("GiveService updated", HTTPStatus.OK)


@give_service_bp.delete('/<int:give_service_id>')
def delete_give_service(give_service_id: int) -> Response:
    """
    Delete give service by ID
    ---
    tags:
      - GiveService
    parameters:
      - in: path
        name: give_service_id
        required: true
        type: integer
        description: Give service ID
    responses:
      200:
        description: Give service deleted successfully
      404:
        description: Give service not found
    """
    give_service_controller.delete(give_service_id)
    return make_response("GiveService deleted", HTTPStatus.OK)
