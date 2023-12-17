from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: str
    position: str



class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    # tasks: int

    # class Config:
    #     orm_mode = True


class TaskBase(BaseModel):
    name: str
    time_limit_hours: int
    status: str


class TaskCreate(TaskBase):
    password: str


class Task(TaskBase):
    id: int
    related_task: int
    employee: int
    # owner: list[Employee] = []

    # class Config:
    #     orm_mode = True