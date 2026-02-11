from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    position: str
    email: str
    phone: Optional[str] = None
    start_date: date = date.today()
    end_date: Optional[date] = None
    is_active: bool = True
