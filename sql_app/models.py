from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base


class Employee(Base):
    """Модель сотрудников"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    patronymic_name = Column(String, nullable=False)
    position = Column(String)

    # tasks = relationship("Task", back_populates="owner")


class Task(Base):
    """Модель задач"""
    __tablename__ = "tasks"

    METHODS = [
        ("waiting", "в ожидании"),
        ("work", "в работе"),
        ("finished", "завершена")
    ]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    related_task = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    employee = Column(Integer, ForeignKey("employees.id"), nullable=True)
    time_limit_hours = Column(Integer)
    status = Column(String, nullable=False, default="waiting")

    # owner = relationship("Employee", back_populates="tasks")
