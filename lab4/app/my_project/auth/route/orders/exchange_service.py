from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import exchange_service_controller
from my_project.auth.domain import ExchangeService

exchange_service_bp = Blueprint('ExchangeService', __name__, url_prefix='/exchange-service')


@exchange_service_bp.get('')
def get_all_exchange_service() -> Response:
    """
    Get all exchange services
    ---
    tags:
      - ExchangeService
    responses:
      200:
        description: List of all exchange services
    """
    return make_response(jsonify(exchange_service_controller.find_all()), HTTPStatus.OK)


@exchange_service_bp.post('')
def create_exchange_service() -> Response:
    """
    Create new exchange service
    ---
    tags:
      - ExchangeService
    parameters:
      - in: body
        name: exchange_service
        description: Exchange service data
        required: true
        schema:
          type: object
          properties:
            device_type_id:
              type: integer
              description: Device type ID
            room_location_id:
              type: integer
              description: Room location ID
            status:
              type: string
              description: Current status of exchange
    responses:
      201:
        description: Exchange service created successfully
    """
    content = request.get_json()
    exchange_service = ExchangeService.create_from_dto(content)
    exchange_service_controller.create(exchange_service)
    return make_response(jsonify(exchange_service.put_into_dto()), HTTPStatus.CREATED)


@exchange_service_bp.get('/<int:exchange_service_id>')
def get_exchange_service(exchange_service_id: int) -> Response:
    """
    Get exchange service by ID
    ---
    tags:
      - ExchangeService
    parameters:
      - in: path
        name: exchange_service_id
        type: integer
        required: true
        description: Exchange service ID
    responses:
      200:
        description: Exchange service data
      404:
        description: Exchange service not found
    """
    return make_response(jsonify(exchange_service_controller.find_by_id(exchange_service_id)), HTTPStatus.OK)


@exchange_service_bp.put('/<int:exchange_service_id>')
def update_exchange_service(exchange_service_id: int) -> Response:
    """
    Update exchange service by ID
    ---
    tags:
      - ExchangeService
    parameters:
      - in: path
        name: exchange_service_id
        type: integer
        required: true
        description: Exchange service ID
      - in: body
        name: exchange_service
        required: true
        description: Updated exchange service data
        schema:
          type: object
          properties:
            device_type_id:
              type: integer
            room_location_id:
              type: integer
            status:
              type: string
    responses:
      200:
        description: Exchange service updated successfully
      404:
        description: Exchange service not found
    """
    content = request.get_json()
    exchange_service = ExchangeService.create_from_dto(content)
    exchange_service_controller.update(exchange_service_id, exchange_service)
    return make_response("ExchangeService updated", HTTPStatus.OK)


@exchange_service_bp.patch('/<int:exchange_service_id>')
def patch_exchange_service(exchange_service_id: int) -> Response:
    """
    Partially update exchange service
    ---
    tags:
      - ExchangeService
    parameters:
      - in: path
        name: exchange_service_id
        type: integer
        required: true
      - in: body
        name: exchange_service
        required: true
        description: Partial data for update
        schema:
          type: object
          properties:
            device_type_id:
              type: integer
            room_location_id:
              type: integer
            status:
              type: string
    responses:
      200:
        description: Exchange service updated successfully
      404:
        description: Exchange service not found
    """
    content = request.get_json()
    exchange_service_controller.patch(exchange_service_id, content)
    return make_response("ExchangeService updated", HTTPStatus.OK)


@exchange_service_bp.delete('/<int:exchange_service_id>')
def delete_exchange_service(exchange_service_id: int) -> Response:
    """
    Delete exchange service by ID
    ---
    tags:
      - ExchangeService
    parameters:
      - in: path
        name: exchange_service_id
        required: true
        type: integer
        description: Exchange service ID
    responses:
      200:
        description: Exchange service deleted successfully
      404:
        description: Exchange service not found
    """
    exchange_service_controller.delete(exchange_service_id)
    return make_response("ExchangeService deleted", HTTPStatus.OK)


@exchange_service_bp.get('/get-exchange-by-device-type/<int:room_location_id>')
def get_exchange_by_device_type(room_location_id: int) -> Response:
    """
    Get exchange services by room location ID
    ---
    tags:
      - ExchangeService
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
    responses:
      200:
        description: List of exchange services for this room location
      404:
        description: No exchange services found
    """
    return make_response(
        jsonify(exchange_service_controller.get_exchange_by_device_type(room_location_id)),
        HTTPStatus.OK
    )
