#Project CG
from app.domain.employee import Employee
from typing import List, Optional
from app.infraestructure.employee_repository import EmployeeRepository
# List employees
employees: List[Employee] = [
    Employee(id=1, first_name="Cecilia", last_name="Gutierrez", position="Developer Jr", email="cecilia.gutierrez@example.com", is_active=False),
    Employee(id=2, first_name="Leticia", last_name="Morales", position="Developer senior", email="leticia.morales@example.com", is_active=True),
    Employee(id=3, first_name="Victor", last_name="Reyes", position="Developer senior", email="victor.reyes@example.com", is_active=True),
]


def get_all_employees() -> List[Employee]:
    return EmployeeRepository.get_all()

def get_employees_by_active(is_active: bool) -> List[Employee]:
    return EmployeeRepository.get_by_active(is_active)

def add_employee(emp: Employee) -> Employee:
    return EmployeeRepository.add(emp)