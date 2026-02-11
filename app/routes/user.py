#Project Cecilia Gutierrez

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.infraestructure.database import get_db
from app.domain.employee import Employee
from app.application.employee_service import (
    get_all_employees,
    get_employees_by_active,
    add_employee,
)
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


@router.get("/", response_model=list[Employee])
async def get_users(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.get("/active", response_model=list[Employee])
async def get_active_users(
    is_active: bool = Query(True),
    db: Session = Depends(get_db),
):
    return get_employees_by_active(db, is_active)


@router.post("/", response_model=Employee)
async def create_employee(
    emp: EmployeeCreate,
    db: Session = Depends(get_db),
):
    new_emp = Employee(**emp.model_dump(), id=0)
    return add_employee(db, new_emp)
