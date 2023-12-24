from enum import Enum
from pydantic import BaseModel
from typing import Optional

class EmployeeFree(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: str or None = None

class EmployeeBusy(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: str or None = None

class StatusEnum(str, Enum):
    """Варианты статуса задач"""
    active = "active"
    working = "working"
    stoped = "stoped"
    closed = "closed"


class TaskBase(BaseModel):
    name: str
    time_limit_hours: int
    # Валидация status
    status: Optional[StatusEnum]
    related_task: int or None = None
    employee: int or None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: str or None = None
    position: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass
