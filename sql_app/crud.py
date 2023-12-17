from sqlalchemy.orm import Session

from sql_app import models, schemas

#
# def get_employee(db: Session, employee_id: int):
#     return db.query(models.Employee).filter(models.Employee.id == employee_id).first()
#
#
# def get_employees(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Employee).offset(skip).limit(limit).all()
#
#
# def create_employee(db: Session, employee: schemas.EmployeeCreate):
#     db_employee = models.Employee(first_name=employee.first_name,
#                               second_name=employee.second_name,
#                               patronymic_name=employee.patronymic_name,
#                               position=employee.position)
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee
#
#
# def get_tasks(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, item: schemas.TaskCreate):
    db_task = models.Task(**item.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task