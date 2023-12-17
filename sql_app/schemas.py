from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: str or None = None
    position: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class TaskBase(BaseModel):
    name: str
    time_limit_hours: int
    status: str
    related_task: int or None = None
    employee: int or None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass
