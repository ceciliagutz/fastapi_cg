#Project Cecilia Gutierrez

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.infraestructure.database import engine, Base
from app import models

app = FastAPI(title="FastAPI CG Project")

app.include_router(user_router, prefix="/user", tags=["Users"])


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}
