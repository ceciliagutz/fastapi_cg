#Project Cecilia Gutierrez

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.domain.employee import Employee

router = APIRouter()

employees = [
    Employee(id=1, first_name="Cecilia", last_name="Gutierrez", position="Developer Jr", email="cecilia.gutierrez@example.com", is_active=False),
    Employee(id=2, first_name="Leticia", last_name="Morales", position="Developer senior", email="leticia.morales@example.com", is_active=True),
    Employee(id=3, first_name="Victor", last_name="Reyes", position="Developer senior", email="victor.reyes@example.com", is_active=True),
]
#Get emplooyes
@router.get("/", response_model=list[Employee])
async def get_users():
    return employees
#Get employees active
@router.get("/active", response_model=list[Employee])
async def get_active_users():
    active_employees = [emp for emp in employees if emp.is_active]
    return active_employees
