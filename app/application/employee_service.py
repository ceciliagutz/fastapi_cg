#Project CG

from typing import List
from sqlalchemy.orm import Session
from app.domain.employee import Employee
from app.infraestructure.employee_repository import EmployeeRepository


def get_all_employees(db: Session) -> List[Employee]:
    return EmployeeRepository.get_all(db)


def get_employees_by_active(db: Session, is_active: bool) -> List[Employee]:
    return EmployeeRepository.get_by_active(db, is_active)


def add_employee(db: Session, emp: Employee) -> Employee:
    return EmployeeRepository.add(db, emp)
