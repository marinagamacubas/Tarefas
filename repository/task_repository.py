# app/repositories/task_repository.py

from sqlalchemy.orm import Session
from domain.model.models import task
from abc import ABC, abstractmethod
from typing import List

class ItaskRepository(ABC):
    @abstractmethod
    def create(self, task: task) -> task:
        pass

    @abstractmethod
    def read(self, task_id: int) -> task:
        pass

    @abstractmethod
    def update(self, task: task, task_data: dict) -> task:
        pass

    @abstractmethod
    def delete(self, task: task) -> int:
        pass

    @abstractmethod
    def find_all(self) -> List[task]:
        pass

class taskRepository(ItaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: task) -> task:
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def update(self, task: task, task_data: dict) -> task:
        for key, value in task_data.items():
            if hasattr(task, key):
                setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete(self, task: task) -> int:
        task_id = task.id
        self.session.delete(task)
        self.session.commit()
        return task_id

    def read(self, task_id: int) -> task:
        return self.session.query(task).filter(task.id == task_id).first()

    def find_all(self) -> List[task]:
        return self.session.query(task).all()