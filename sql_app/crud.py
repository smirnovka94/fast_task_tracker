from pydantic import BaseModel
from sqlalchemy import Null

from sqlalchemy.orm import Session
from sql_app.models import Employee, Task
from sql_app.schemas import EmployeeCreate, EmployeeUpdate, TaskCreate, TaskUpdate, EmployeeBusy


# Получение списка  занятых сотрудников
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

def get_free_employees(task, employees):
    # Список закрепленных задач

    # employees = db.query(Employee).all()
    free_employees = []
    free_id_employees = []
    employee_tasts = {}

    for employee in employees:
        # Ищем занятые задачисотрудниками
        tasks = db.query(Task).filter(Task.employee == employee.id).count()
        all_tasks = db.query(Task).all()
        employee.tasks = tasks
        employee_tasts[employee] = tasks

    employee_sorted = sorted(employee_tasts.items(), key=lambda x: x[1])

    results = []
    for keys, values in employee_sorted:
        print(f"{keys.first_name} {values == 0}")
        if values == 0:
            results.append(keys)
        if results == []:
            results = employee_sorted[0]
    return [{"ФИО": f"{result.first_name, result.second_name}"} for result in results]


    #[{"first_name": employee.first_name, "second_name": employee.second_name} for employee in employees]


def get_important_tasks(db: Session):
    employees = db.query(Employee).all()
    employee_tasks = {}
    all_tasks = db.query(Task).all()

    sub_tasks = db.query(Task).filter(Task.related_task != None).all()

    id_parrent_tasks = []
    id_employee_with_parrent_tasks=[]

    for sub_task in sub_tasks:
        # Получаем id родительской задачи
        id_parrent_tasks.append(sub_task.related_task)


    for task in all_tasks:
        if (task.id in id_parrent_tasks) and (task.employee != None):
            id_employee_with_parrent_tasks.append(task.employee)

    # Самый свободный сотрудник
    count_tasks = 100000000
    count_tasks_p = 100000000
    for employee in employees:
        # Ищем количество задач у сотрудника
        tasks = db.query(Task).filter(Task.employee == employee.id).all()
        employee.tasks = len(tasks)
        # Находим наименее занятого
        if int(employee.tasks)<count_tasks:
            count_tasks = len(tasks)
            free_employee = employee

        # Ищем незагруженного сотрудника с родительскими задачами
        if employee.id in id_employee_with_parrent_tasks:
            if int(employee.tasks)<count_tasks_p:
                count_tasks_p = employee.tasks
                free_employee_with_parrent_tasks = employee


        employee.list_id_tasks = [task.id for task in tasks]
        employee_tasks[employee] = len(tasks)
    # сортируем employee по возрастанию занятости
    employee_sorted = sorted(employee_tasks.items(), key=lambda x: x[1])

    # Ищем наиболее подходящего кандидата
    if int(free_employee_with_parrent_tasks.tasks) <= int(free_employee.tasks) + 2:
        ideal_employee = free_employee_with_parrent_tasks
    else:
        ideal_employee = free_employee

    # print(f"id_employee_with_parrent_tasks {id_employee_with_parrent_tasks}")
    #
    # print(f"Свободный сотрудник {free_employee.first_name}-{free_employee.tasks}")
    # print(f"Малозагруженный родительский сотрудник {free_employee_with_parrent_tasks.first_name}-{free_employee_with_parrent_tasks.tasks}")


    # Получаем зависимые задачи, которые уже в работе
    sub_tasks = db.query(Task).filter((Task.related_task != None) & (Task.status == "working")).all()
    # id_parrent_tasks
    # Получаем активные задачи
    parrent_tasks = []

    tasks_active = db.query(Task).filter(Task.status == "active").all()
    for task in tasks_active:
        # db.query(Employee).filter(Employee.id == employee.id).count()

        if task.id in id_parrent_tasks:
            if ideal_employee.patronymic_name == None:
                task.employees = [ideal_employee.first_name, ideal_employee.second_name]
            else:
                task.employees = [ideal_employee.first_name, ideal_employee.second_name, ideal_employee.patronymic_name]
            filter_task = {"Важная задача": task.name, "Срок": task.time_limit_hours,"ФИО сотрудника": task.employees}
            parrent_tasks.append(filter_task)

    return parrent_tasks


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
