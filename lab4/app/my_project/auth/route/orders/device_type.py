from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import device_type_controller
from lab4.app.my_project.auth.domain import DeviceType

device_type_bp = Blueprint('DeviceType', __name__, url_prefix='/device-type')


@device_type_bp.get('')
def get_all_device_type() -> Response:
    """
    Get all device types
    ---
    tags:
      - DeviceType
    responses:
      200:
        description: List of all device types
    """
    return make_response(jsonify(device_type_controller.find_all()), HTTPStatus.OK)


@device_type_bp.post('')
def create_device_type() -> Response:
    """
    Create new device type
    ---
    tags:
      - DeviceType
    parameters:
      - in: body
        name: device_type
        description: Device type data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Device type name
            description:
              type: string
              description: Detailed description
    responses:
      201:
        description: Device type created successfully
    """
    content = request.get_json()
    device_type = DeviceType.create_from_dto(content)
    device_type_controller.create(device_type)
    return make_response(jsonify(device_type.put_into_dto()), HTTPStatus.CREATED)


@device_type_bp.get('/<int:device_type_id>')
def get_device_type(device_type_id: int) -> Response:
    """
    Get device type by ID
    ---
    tags:
      - DeviceType
    parameters:
      - in: path
        name: device_type_id
        type: integer
        required: true
        description: Device type ID
    responses:
      200:
        description: Device type data
      404:
        description: Device type not found
    """
    return make_response(jsonify(device_type_controller.find_by_id(device_type_id)), HTTPStatus.OK)


@device_type_bp.put('/<int:device_type_id>')
def update_device_type(device_type_id: int) -> Response:
    """
    Update device type by ID
    ---
    tags:
      - DeviceType
    parameters:
      - in: path
        name: device_type_id
        type: integer
        required: true
        description: Device type ID
      - in: body
        name: device_type
        description: Updated device type data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
    responses:
      200:
        description: Device type updated successfully
      404:
        description: Device type not found
    """
    content = request.get_json()
    device_type = DeviceType.create_from_dto(content)
    device_type_controller.update(device_type_id, device_type)
    return make_response("DeviceType updated", HTTPStatus.OK)


@device_type_bp.patch('/<int:device_type_id>')
def patch_device_type(device_type_id: int) -> Response:
    """
    Partially update device type by ID
    ---
    tags:
      - DeviceType
    parameters:
      - in: path
        name: device_type_id
        type: integer
        required: true
        description: Device type ID
      - in: body
        name: device_type
        description: Partial device type data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
    responses:
      200:
        description: Device type updated successfully
      404:
        description: Device type not found
    """
    content = request.get_json()
    device_type_controller.patch(device_type_id, content)
    return make_response("DeviceType updated", HTTPStatus.OK)


@device_type_bp.delete('/<int:device_type_id>')
def delete_device_type(device_type_id: int) -> Response:
    """
    Delete device type by ID
    ---
    tags:
      - DeviceType
    parameters:
      - in: path
        name: device_type_id
        type: integer
        required: true
        description: Device type ID
    responses:
      200:
        description: Device type deleted successfully
      404:
        description: Device type not found
    """
    device_type_controller.delete(device_type_id)
    return make_response("DeviceType deleted", HTTPStatus.OK)
