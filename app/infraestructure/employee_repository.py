#Project CG

from typing import List
from sqlalchemy.orm import Session
from app.models import EmployeeModel
from app.domain.employee import Employee


class EmployeeRepository:

    @staticmethod
    def get_all(db: Session) -> List[Employee]:
        employees = db.query(EmployeeModel).all()
        return [
            Employee(
                id=e.id,
                first_name=e.first_name,
                last_name=e.last_name,
                position=e.position,
                email=e.email,
                phone=e.phone,
                is_active=e.is_active,
            )
            for e in employees
        ]

    @staticmethod
    def get_by_active(db: Session, is_active: bool) -> List[Employee]:
        employees = (
            db.query(EmployeeModel)
            .filter(EmployeeModel.is_active == is_active)
            .all()
        )
        return [
            Employee(
                id=e.id,
                first_name=e.first_name,
                last_name=e.last_name,
                position=e.position,
                email=e.email,
                phone=e.phone,
                is_active=e.is_active,
            )
            for e in employees
        ]

    @staticmethod
    def add(db: Session, emp: Employee) -> Employee:
        db_emp = EmployeeModel(
            first_name=emp.first_name,
            last_name=emp.last_name,
            position=emp.position,
            email=emp.email,
            phone=emp.phone,
            is_active=emp.is_active,
        )
        db.add(db_emp)
        db.commit()
        db.refresh(db_emp)

        return Employee(
            id=db_emp.id,
            first_name=db_emp.first_name,
            last_name=db_emp.last_name,
            position=db_emp.position,
            email=db_emp.email,
            phone=db_emp.phone,
            is_active=db_emp.is_active,
        )
