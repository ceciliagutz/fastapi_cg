#Project Cecilia Gutierrez

from fastapi import APIRouter, Query
from app.domain.employee import Employee
from app.application.employee_service import get_all_employees, get_employees_by_active, add_employee
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    position: str
    email: str
    phone: Optional[str] = None
    is_active: bool = True

# Endpoints
@router.get("/", response_model=list[Employee])
async def get_users():
    return get_all_employees()

@router.get("/active", response_model=list[Employee])
async def get_active_users(is_active: bool = Query(True, description="Filter by active status")):
    return get_employees_by_active(is_active)

@router.post("/", response_model=Employee)
async def create_employee(emp: EmployeeCreate):
    new_emp = Employee(**emp.dict(), id=0)  
    return add_employee(new_emp)
