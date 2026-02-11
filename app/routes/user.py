#Project Cecilia Gutierrez

from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.domain.employee import Employee
from pydantic import BaseModel
from typing import Optional


router = APIRouter()

employees = [
    Employee(id=1, first_name="Cecilia", last_name="Gutierrez", position="Developer Jr", email="cecilia.gutierrez@example.com", is_active=False),
    Employee(id=2, first_name="Leticia", last_name="Morales", position="Developer senior", email="leticia.morales@example.com", is_active=True),
    Employee(id=3, first_name="Victor", last_name="Reyes", position="Developer senior", email="victor.reyes@example.com", is_active=True),
]

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    position: str
    email: str
    phone: Optional[str] = None
    is_active: bool = True

# GET all employes
@router.get("/", response_model=list[Employee])
async def get_all_employees():
    return employees

# GET active o desactive
@router.get("/active", response_model=list[Employee])
async def get_active_users(is_active: bool = Query(True, description="Filter by active status")):
    return [emp for emp in employees if emp.is_active == is_active]

# POST create new employee
@router.post("/", response_model=Employee)
async def create_employee(emp: EmployeeCreate):
    new_id = max([e.id for e in employees]) + 1 if employees else 1
    new_emp = Employee(id=new_id, **emp.dict())
    employees.append(new_emp)
    return new_emp

# DELETE delete employee
@router.delete("/{id}", response_model=dict)
async def delete_employee(id: int):
    for emp in employees:
        if emp.id == id:
            employees.remove(emp)
            return {"message": f"Employee with id {id} deleted"}
    raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")