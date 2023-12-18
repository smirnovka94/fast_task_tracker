from sqlalchemy import Column, ForeignKey, Integer, String
from sql_app.database import Base


class Employee(Base):
    """Модель сотрудников"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    patronymic_name = Column(String, nullable=True)
    position = Column(String)


class Task(Base):
    """Модель задач"""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    related_task = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    employee = Column(Integer, ForeignKey("employees.id"), nullable=True)
    time_limit_hours = Column(Integer)
    status = Column(String, nullable=False, default="waiting")
