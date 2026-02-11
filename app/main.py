#Project Cecilia Gutierrez

from fastapi import FastAPI
from app.routes import user

app = FastAPI(title= "FastAPI CG Project")

app.include_router(user.router, prefix="/user", tags=["User"])

@app.get("/")
async def root():
    return{"message": "API is running"}


