#Project CG

from app.domain.employee import Employee
from typing import List

# Simulator db
_employee_db: List[Employee] = [
    Employee(id=1, first_name="Cecilia", last_name="Gutierrez", position="Developer Jr", email="cecilia.gutierrez@example.com", is_active=False),
    Employee(id=2, first_name="Leticia", last_name="Morales", position="Developer senior", email="leticia.morales@example.com", is_active=True),
    Employee(id=3, first_name="Victor", last_name="Reyes", position="Developer senior", email="victor.reyes@example.com", is_active=True),
]

class EmployeeRepository:

    @staticmethod
    def get_all() -> List[Employee]:
        return _employee_db

    @staticmethod
    def get_by_active(is_active: bool) -> List[Employee]:
        return [emp for emp in _employee_db if emp.is_active == is_active]

    @staticmethod
    def add(emp: Employee) -> Employee:
        new_id = max([e.id for e in _employee_db]) + 1 if _employee_db else 1
        emp.id = new_id
        _employee_db.append(emp)
        return emp
