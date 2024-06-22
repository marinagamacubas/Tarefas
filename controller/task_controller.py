from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from domain.dto.dtos import taskDTO, taskCreateDTO, taskUpdateDTO
from repository.task_repository import taskRepository
from service.task_service import taskService
from config.database import get_db

task_router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_task_repo(db: Session = Depends(get_db)) -> taskRepository:
    return taskRepository(db)

@task_router.post("/", status_code=201, description="Create a new task", response_model=taskDTO)
def create_task(request: taskCreateDTO, task_repo: taskRepository = Depends(get_task_repo)):
    task_service = taskService(task_repo)
    return task_service.create_task(request)

@task_router.get("/{task_id}", status_code=200, description="Get a task by ID", response_model=taskDTO)
def find_task_by_id(task_id: int, task_repo: taskRepository = Depends(get_task_repo)):
    task_service = taskService(task_repo)
    return task_service.read_task(task_id)

@task_router.get("/", status_code=200, description="Get all tasks", response_model=List[taskDTO])
def find_all_tasks(task_repo: taskRepository = Depends(get_task_repo)):
    task_service = taskService(task_repo)
    return task_service.find_all()

@task_router.put("/{task_id}", status_code=200, description="Update a task", response_model=taskDTO)
def update_task(task_id: int, request: taskUpdateDTO, task_repo: taskRepository = Depends(get_task_repo)):
    task_service = taskService(task_repo)
    return task_service.update_task(task_id, request)

@task_router.delete("/{task_id}", status_code=204, description="Delete a task")
def delete_task(task_id: int, task_repo: taskRepository = Depends(get_task_repo)):
    task_service = taskService(task_repo)
    task_service.delete_task(task_id)
    return {"message": "Task deleted successfully"}
