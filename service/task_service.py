import logging
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from domain.dto.dtos import taskCreateDTO, taskDTO, taskUpdateDTO
from domain.model.models import task
from repository.task_repository import ItaskRepository

logger = logging.getLogger("fastapi")


class ItaskService:
    def create_task(self, task_data: taskCreateDTO) -> taskDTO:
        raise NotImplementedError

    def read_task(self, task_id: int) -> taskDTO:
        raise NotImplementedError

    def update_task(self, task_id: int, task_update: taskUpdateDTO) -> taskDTO:
        raise NotImplementedError

    def delete_task(self, task_id: int) -> int:
        raise NotImplementedError

    def find_all(self) -> list[taskDTO]:
        raise NotImplementedError


class taskService(ItaskService):
    def __init__(self, task_repository: ItaskRepository):
        self.task_repository = task_repository

    def create_task(self, task_data: taskCreateDTO) -> taskDTO:
        task_model = task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status
        )
        try:
            logger.info("Creating task: %s", task_model)
            created_task = self.task_repository.create(task_model)
        except IntegrityError as e:
            logger.error("Error creating task: %s. Detail: %s", task_model, e)
            raise HTTPException(status_code=409, detail=f"Task already exists. Error: {e.args[0]}")
        return taskDTO(**created_task.__dict__)

    def read_task(self, task_id: int) -> taskDTO:
        logger.info("Reading task with id %s", task_id)
        task_model = self.task_repository.read(task_id)
        if task_model is None:
            logger.error("Task with id %s not found", task_id)
            raise HTTPException(status_code=404, detail="Task not found")
        return taskDTO(**task_model.__dict__)

    def update_task(self, task_id: int, task_update: taskUpdateDTO) -> taskDTO:
        logger.info("Updating task with id %s", task_id)
        task_model = self.task_repository.read(task_id)
        if task_model is None:
            logger.error("Task with id %s not found", task_id)
            raise HTTPException(status_code=404, detail="Task not found")

        task_data_dict = task_update.dict(exclude_unset=True)
        for key, value in task_data_dict.items():
            setattr(task_model, key, value)

        updated_task = self.task_repository.update(task_model, task_data_dict)
        return taskDTO(**updated_task.__dict__)

    def delete_task(self, task_id: int) -> int:
        logger.info("Deleting task with id %s", task_id)
        task_model = self.task_repository.read(task_id)
        if task_model is None:
            logger.error("Task with id %s not found", task_id)
            raise HTTPException(status_code=404, detail="Task not found")
        return self.task_repository.delete(task_model)

    def find_all(self) -> list[taskDTO]:
        logger.info("Finding all tasks")
        tasks = self.task_repository.find_all()
        return [taskDTO(**task.__dict__) for task in tasks]
