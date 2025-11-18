from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import employee_controller
from lab4.app.my_project.auth.domain import Employee

employee_bp = Blueprint('Employee', __name__, url_prefix='/employee')


@employee_bp.get('')
def get_all_employee() -> Response:
    """
    Get all employees
    ---
    tags:
      - Employee
    responses:
      200:
        description: List of all employees
    """
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)


@employee_bp.post('')
def create_employee() -> Response:
    """
    Create new employee
    ---
    tags:
      - Employee
    parameters:
      - in: body
        name: employee
        description: Employee data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Full name
            position:
              type: string
              description: Job position
            department:
              type: string
              description: Department name
            salary:
              type: number
              description: Salary value
    responses:
      201:
        description: Employee created successfully
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)


@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    """
    Get employee by ID
    ---
    tags:
      - Employee
    parameters:
      - in: path
        name: employee_id
        type: integer
        required: true
        description: Employee ID
    responses:
      200:
        description: Employee data
      404:
        description: Employee not found
    """
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)


@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    """
    Update employee by ID
    ---
    tags:
      - Employee
    parameters:
      - in: path
        name: employee_id
        type: integer
        required: true
        description: Employee ID
      - in: body
        name: employee
        description: Updated employee data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            position:
              type: string
            department:
              type: string
            salary:
              type: number
    responses:
      200:
        description: Employee updated successfully
      404:
        description: Employee not found
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.patch('/<int:employee_id>')
def patch_employee(employee_id: int) -> Response:
    """
    Partially update employee by ID
    ---
    tags:
      - Employee
    parameters:
      - in: path
        name: employee_id
        type: integer
        required: true
        description: Employee ID
      - in: body
        name: employee
        description: Partial employee data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            position:
              type: string
            department:
              type: string
            salary:
              type: number
    responses:
      200:
        description: Employee updated successfully
      404:
        description: Employee not found
    """
    content = request.get_json()
    employee_controller.patch(employee_id, content)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    """
    Delete employee by ID
    ---
    tags:
      - Employee
    parameters:
      - in: path
        name: employee_id
        type: integer
        required: true
        description: Employee ID
    responses:
      200:
        description: Employee deleted successfully
      404:
        description: Employee not found
    """
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)
