#Project CG
from app.domain.employee import Employee
from typing import List, Optional

# List employees
employees: List[Employee] = [
    Employee(id=1, first_name="Cecilia", last_name="Gutierrez", position="Developer Jr", email="cecilia.gutierrez@example.com", is_active=False),
    Employee(id=2, first_name="Leticia", last_name="Morales", position="Developer senior", email="leticia.morales@example.com", is_active=True),
    Employee(id=3, first_name="Victor", last_name="Reyes", position="Developer senior", email="victor.reyes@example.com", is_active=True),
]


def get_all_employees() -> List[Employee]:
    return employees

def get_employees_by_active(is_active: bool) -> List[Employee]:
    return [emp for emp in employees if emp.is_active == is_active]

def add_employee(emp: Employee) -> Employee:
    new_id = max([e.id for e in employees]) + 1 if employees else 1
    emp.id = new_id
    employees.append(emp)
    return emp