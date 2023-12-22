

# Занятые сотрудники
@app.get("/employees/busy")
def get_busy_employees(db: Session = Depends(get_db)):
    """Получаем список занятых сотрудников"""
    items = crud.get_busy_employees(db)
    return items

# Важные задачи
@app.get("/tasks/actite")
def read_employees(db: Session = Depends(get_db)):
    """Получаем список занятых сотрудников"""
    items = crud.get_busy_employees(db)
    return items

# CRUD для Employees
@app.post("/employee")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.get("/employee/{employee_id}")
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.put("/employee/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.update_employee(db=db, db_employee=db_employee, employee=employee)


@app.delete("/employee/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    crud.delete_employee(db=db, db_employee=db_employee)


# CRUD для Tasks
@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    """Получаем список существующих задач"""
    items = crud.get_tasks(db)
    return items


@app.post("/task/create")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.get("/task/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/task/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db=db, db_task=db_task, task=task)


@app.delete("/task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db=db, db_task=db_task)