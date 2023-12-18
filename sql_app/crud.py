from sqlalchemy.orm import Session
from sql_app.models import Employee, Task
from sql_app.schemas import EmployeeCreate, EmployeeUpdate, TaskCreate, TaskUpdate


# Получение списка сотрудников
def get_busy_employees(db: Session, status="active"):
    employees = db.query(Employee).all()
    # Получаем количество задач у каждого сотрудника
    myDict = dict()

    for employee in employees:
        # Количество активных задач
        task_count = db.query(Task).filter((Task.employee == employee.id) and (Task.status == status)).count()
        employee.task_count = task_count
        # Список активных задач
        tasks = db.query(Task).filter((Task.employee == employee.id) & (Task.status == status)).all()
        employee.tasks = tasks

        task_sum = []
        for task in tasks:
            task_sum.append(task)
        myDict.setdefault(employee, []).append(task_count)
        sorted_dict = sorted(myDict.items(), key=lambda x: x[1])
    sort_employees = []
    for key, value in sorted_dict:
        sort_employees.append(key)

    return sort_employees


# Создание сотрудника
def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(first_name=employee.first_name,
                           second_name=employee.second_name,
                           patronymic_name=employee.patronymic_name,
                           position=employee.position)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# Получение информации о сотруднике по id
def get_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    task_count = db.query(Task).filter(Task.employee == employee.id).count()
    employee.task_count = task_count
    return employee


# Обновление информации о сотруднике
def update_employee(db: Session, db_employee: Employee, employee: EmployeeUpdate):
    db_employee.first_name = employee.first_name
    db_employee.last_name = employee.last_name
    db.commit()
    db.refresh(db_employee)
    return db_employee


# Удаление сотрудника
def delete_employee(db: Session, db_employee: Employee):
    db.delete(db_employee)
    db.commit()


# Получение списка задач
def get_tasks(db: Session):
    return db.query(Task).all()


# Создание задачи
def create_task(db: Session, task: TaskCreate):
    db_task = Task(name=task.name,
                   related_task=task.related_task,
                   employee=task.employee,
                   time_limit_hours=task.time_limit_hours,
                   status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Получение информации о задаче по id
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


# Обновление информации о задаче
def update_task(db: Session, db_task: Task, task: TaskUpdate):
    db_task.name = task.name
    db_task.related_task = task.related_task
    db_task.employee = task.employee
    db.commit()
    db.refresh(db_task)
    return db_task


# Удаление задачи
def delete_task(db: Session, db_task: Task):
    db.delete(db_task)
    db.commit()
