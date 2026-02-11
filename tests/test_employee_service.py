import pytest
from app.domain.employee import Employee
from app.application import employee_service

def test_get_all_employees():
    employees = employee_service.get_all_employees()
    assert len(employees) >= 3  
    assert any(emp.first_name == "Cecilia" for emp in employees)

def test_get_employees_by_active():
    active_emps = employee_service.get_employees_by_active(True)
    inactive_emps = employee_service.get_employees_by_active(False)

    
    assert all(emp.is_active for emp in active_emps)
    assert all(not emp.is_active for emp in inactive_emps)

def test_add_employee():
    new_emp = Employee(id=0, first_name="Ana", last_name="Lopez", position="Tester", email="ana.lopez@example.com", is_active=True)
    added_emp = employee_service.add_employee(new_emp)

   
    assert added_emp.id != 0
    
    all_emps = employee_service.get_all_employees()
    assert added_emp in all_emps
