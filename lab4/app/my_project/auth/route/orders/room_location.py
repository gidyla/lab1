from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import room_location_controller
from my_project.auth.domain import RoomLocation

room_location_bp = Blueprint('RoomLocation', __name__, url_prefix='/room-location')


@room_location_bp.get('')
def get_all_room_location() -> Response:
    """
    Get all room locations
    ---
    tags:
      - RoomLocation
    responses:
      200:
        description: List of all room locations
    """
    return make_response(jsonify(room_location_controller.find_all()), HTTPStatus.OK)


@room_location_bp.post('')
def create_room_location() -> Response:
    """
    Create new room location
    ---
    tags:
      - RoomLocation
    parameters:
      - in: body
        name: room_location
        required: true
        description: Room location data
        schema:
          type: object
          properties:
            room_number:
              type: string
              description: Room number or identifier
            office_location_id:
              type: integer
              description: ID of related office location
            floor:
              type: integer
              description: Floor number
    responses:
      201:
        description: Room location created successfully
    """
    content = request.get_json()
    room_location = RoomLocation.create_from_dto(content)
    room_location_controller.create(room_location)
    return make_response(jsonify(room_location.put_into_dto()), HTTPStatus.CREATED)


@room_location_bp.get('/<int:room_location_id>')
def get_room_location(room_location_id: int) -> Response:
    """
    Get room location by ID
    ---
    tags:
      - RoomLocation
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
    responses:
      200:
        description: Room location data
      404:
        description: Room location not found
    """
    return make_response(jsonify(room_location_controller.find_by_id(room_location_id)), HTTPStatus.OK)


@room_location_bp.put('/<int:room_location_id>')
def update_room_location(room_location_id: int) -> Response:
    """
    Update room location
    ---
    tags:
      - RoomLocation
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
      - in: body
        name: room_location
        required: true
        description: Updated room location data
        schema:
          type: object
          properties:
            room_number:
              type: string
            office_location_id:
              type: integer
            floor:
              type: integer
    responses:
      200:
        description: Room location updated successfully
      404:
        description: Room location not found
    """
    content = request.get_json()
    room_location = RoomLocation.create_from_dto(content)
    room_location_controller.update(room_location_id, room_location)
    return make_response("RoomLocation updated", HTTPStatus.OK)


@room_location_bp.patch('/<int:room_location_id>')
def patch_room_location(room_location_id: int) -> Response:
    """
    Partially update room location
    ---
    tags:
      - RoomLocation
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
      - in: body
        name: room_location
        description: Partial room location data
        required: true
        schema:
          type: object
          properties:
            room_number:
              type: string
            office_location_id:
              type: integer
            floor:
              type: integer
    responses:
      200:
        description: Room location updated successfully
      404:
        description: Room location not found
    """
    content = request.get_json()
    room_location_controller.patch(room_location_id, content)
    return make_response("RoomLocation updated", HTTPStatus.OK)


@room_location_bp.delete('/<int:room_location_id>')
def delete_room_location(room_location_id: int) -> Response:
    """
    Delete room location
    ---
    tags:
      - RoomLocation
    parameters:
      - in: path
        name: room_location_id
        type: integer
        required: true
        description: Room location ID
    responses:
      200:
        description: Room location deleted successfully
      404:
        description: Room location not found
    """
    room_location_controller.delete(room_location_id)
    return make_response("RoomLocation deleted", HTTPStatus.OK)
