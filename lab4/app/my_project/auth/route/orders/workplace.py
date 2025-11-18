from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import workplace_controller
from lab4.app.my_project.auth.domain import Workplace

workplace_bp = Blueprint('Workplace', __name__, url_prefix='/workplace')


@workplace_bp.get('')
def get_all_workplace() -> Response:
    """
    Get all workplaces
    ---
    tags:
      - Workplace
    responses:
      200:
        description: List of all workplaces
    """
    return make_response(jsonify(workplace_controller.find_all()), HTTPStatus.OK)


@workplace_bp.post('')
def create_workplace() -> Response:
    """
    Create new workplace
    ---
    tags:
      - Workplace
    parameters:
      - in: body
        name: workplace
        required: true
        description: Workplace data
        schema:
          type: object
          properties:
            employee_id:
              type: integer
              description: Employee assigned to workplace
            office_location_id:
              type: integer
              description: Office location ID
            room_location_id:
              type: integer
              description: Room location ID
    responses:
      201:
        description: Workplace created successfully
    """
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.create(workplace)
    return make_response(jsonify(workplace.put_into_dto()), HTTPStatus.CREATED)


@workplace_bp.get('/<int:workplace_id>')
def get_workplace(workplace_id: int) -> Response:
    """
    Get workplace by ID
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: workplace_id
        type: integer
        required: true
        description: Workplace ID
    responses:
      200:
        description: Workplace data
      404:
        description: Workplace not found
    """
    return make_response(jsonify(workplace_controller.find_by_id(workplace_id)), HTTPStatus.OK)


@workplace_bp.put('/<int:workplace_id>')
def update_workplace(workplace_id: int) -> Response:
    """
    Update workplace
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: workplace_id
        required: true
        type: integer
        description: Workplace ID
      - in: body
        name: workplace
        description: Updated workplace data
        required: true
        schema:
          type: object
          properties:
            employee_id:
              type: integer
            office_location_id:
              type: integer
            room_location_id:
              type: integer
    responses:
      200:
        description: Workplace updated successfully
      404:
        description: Workplace not found
    """
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.update(workplace_id, workplace)
    return make_response("Workplace updated", HTTPStatus.OK)


@workplace_bp.patch('/<int:workplace_id>')
def patch_workplace(workplace_id: int) -> Response:
    """
    Partially update workplace
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: workplace_id
        required: true
        type: integer
      - in: body
        name: workplace
        description: Partial workplace data
        required: true
        schema:
          type: object
          properties:
            employee_id:
              type: integer
            office_location_id:
              type: integer
            room_location_id:
              type: integer
    responses:
      200:
        description: Workplace updated successfully
      404:
        description: Workplace not found
    """
    content = request.get_json()
    workplace_controller.patch(workplace_id, content)
    return make_response("Workplace updated", HTTPStatus.OK)


@workplace_bp.delete('/<int:workplace_id>')
def delete_workplace(workplace_id: int) -> Response:
    """
    Delete workplace by ID
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: workplace_id
        required: true
        type: integer
        description: Workplace ID
    responses:
      200:
        description: Workplace deleted successfully
      404:
        description: Workplace not found
    """
    workplace_controller.delete(workplace_id)
    return make_response("Workplace deleted", HTTPStatus.OK)


@workplace_bp.get('/get-employee-by-office/<int:office_location_id>')
def get_employee_by_office(office_location_id: int) -> Response:
    """
    Get employee list for given office location
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: office_location_id
        required: true
        type: integer
        description: Office location ID
    responses:
      200:
        description: List of employees in this office
      404:
        description: No employees found for this office
    """
    return make_response(
        jsonify(workplace_controller.get_employee_by_office(office_location_id)),
        HTTPStatus.OK
    )


@workplace_bp.get('/get-office-by-employee/<int:employee_id>')
def get_office_by_employee(employee_id: int) -> Response:
    """
    Get office location for a given employee
    ---
    tags:
      - Workplace
    parameters:
      - in: path
        name: employee_id
        required: true
        type: integer
        description: Employee ID
    responses:
      200:
        description: Office assigned to the employee
      404:
        description: No office found for this employee
    """
    return make_response(
        jsonify(workplace_controller.get_office_by_employee(employee_id)),
        HTTPStatus.OK
    )
