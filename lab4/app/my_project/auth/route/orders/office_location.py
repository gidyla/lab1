from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import office_location_controller
from my_project.auth.domain import OfficeLocation

office_location_bp = Blueprint('OfficeLocation', __name__, url_prefix='/office-location')


@office_location_bp.get('')
def get_all_office_location() -> Response:
    """
    Get all office locations
    ---
    tags:
      - OfficeLocation
    responses:
      200:
        description: List of all office locations
    """
    return make_response(jsonify(office_location_controller.find_all()), HTTPStatus.OK)


@office_location_bp.post('')
def create_office_location() -> Response:
    """
    Create new office location
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: body
        name: office_location
        required: true
        description: Office location data
        schema:
          type: object
          properties:
            office_name:
              type: string
              description: Name of the office
            address:
              type: string
              description: Office address
            floor:
              type: integer
              description: Location floor number
    responses:
      201:
        description: Office location created successfully
    """
    content = request.get_json()
    office_location = OfficeLocation.create_from_dto(content)
    office_location_controller.create(office_location)
    return make_response(jsonify(office_location.put_into_dto()), HTTPStatus.CREATED)


@office_location_bp.get('/<int:office_location_id>')
def get_office_location(office_location_id: int) -> Response:
    """
    Get office location by ID
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: path
        name: office_location_id
        type: integer
        required: true
        description: Office location ID
    responses:
      200:
        description: Office location data
      404:
        description: Office location not found
    """
    return make_response(jsonify(office_location_controller.find_by_id(office_location_id)), HTTPStatus.OK)


@office_location_bp.put('/<int:office_location_id>')
def update_office_location(office_location_id: int) -> Response:
    """
    Update office location
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: path
        name: office_location_id
        type: integer
        required: true
        description: Office location ID
      - in: body
        name: office_location
        description: Updated office location data
        required: true
        schema:
          type: object
          properties:
            office_name:
              type: string
            address:
              type: string
            floor:
              type: integer
    responses:
      200:
        description: Office location updated successfully
      404:
        description: Office location not found
    """
    content = request.get_json()
    office_location = OfficeLocation.create_from_dto(content)
    office_location_controller.update(office_location_id, office_location)
    return make_response("OfficeLocation updated", HTTPStatus.OK)


@office_location_bp.patch('/<int:office_location_id>')
def patch_office_location(office_location_id: int) -> Response:
    """
    Partially update office location
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: path
        name: office_location_id
        required: true
        type: integer
        description: Office location ID
      - in: body
        name: office_location
        description: Partial data for update
        required: true
        schema:
          type: object
          properties:
            office_name:
              type: string
            address:
              type: string
            floor:
              type: integer
    responses:
      200:
        description: Office location updated successfully
      404:
        description: Office location not found
    """
    content = request.get_json()
    office_location_controller.patch(office_location_id, content)
    return make_response("OfficeLocation updated", HTTPStatus.OK)


@office_location_bp.delete('/<int:office_location_id>')
def delete_office_location(office_location_id: int) -> Response:
    """
    Delete office location by ID
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: path
        name: office_location_id
        required: true
        type: integer
        description: Office location ID
    responses:
      200:
        description: Office location deleted successfully
      404:
        description: Office location not found
    """
    office_location_controller.delete(office_location_id)
    return make_response("OfficeLocation deleted", HTTPStatus.OK)


@office_location_bp.get('/get-office-by-room/<int:room_location_id>')
def get_office_by_room(room_location_id: int) -> Response:
    """
    Get office location based on room location ID
    ---
    tags:
      - OfficeLocation
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
    responses:
      200:
        description: Office data for given room
      404:
        description: No matching office found
    """
    return make_response(
        jsonify(office_location_controller.get_office_by_room(room_location_id)),
        HTTPStatus.OK
    )
