from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    return [{"id":1, "name": "Cecilia Guadalupe", "lastname": "Gutierrez Urbano", "phone": 5515765737}, {"id": 2, "name": "Leticia", "lastname": "Morales Martinon", "phone": 5514223645}]