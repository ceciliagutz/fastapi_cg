#Project Cecilia Gutierrez

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.models import Base
from app.infraestructure.database import engine

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["Users"])

@app.get("/")
def root():
    return {"message": "API is running"}


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
