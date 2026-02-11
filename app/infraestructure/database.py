#Project Cecilia Gutierrez

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("Database_url", "postgresql+asyncpg://user:password@localhost/dbname")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind = engine, 
    expire_on_commit=False,
    class_=AsyncSession
)

Base= declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
                         