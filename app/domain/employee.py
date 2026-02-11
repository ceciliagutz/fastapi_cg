
from datetime import date
from typing import Optional
from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    position: str
    email: str
    phone: Optional[str] = None
    start_date: Optional[date] = date.today()
    end_date: Optional[date] = None
    is_active: bool = True
