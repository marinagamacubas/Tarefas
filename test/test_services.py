import pytest
from sqlalchemy.orm import Session
from service.task_service import taskService
from repository.task_repository import taskRepository
from domain.dto.dtos import taskCreateDTO, taskUpdateDTO

@pytest.fixture(scope="module")
def service():
    """Fixture para instanciar o serviço de tarefas."""
    return taskService(taskRepository)

def test_create_task(service: taskService, db: Session):
    """Teste para o método create_task do serviço."""
    task_data = taskCreateDTO(title="Teste de Tarefa", description="Testando a criação de tarefa")

    created_task = service.create_task(task_data)

    assert created_task.title == task_data.title
    assert created_task.description == task_data.description

def test_update_task(service: taskService, db: Session):
    """Teste para o método update_task do serviço."""
    task_id = 1
    updated_data = taskUpdateDTO(title="Tarefa Atualizada", description="Descrição da tarefa atualizada", status="Concluída")

    updated_task = service.update_task(task_id, updated_data)

    assert updated_task.title == updated_data.title
    assert updated_task.description == updated_data.description
    assert updated_task.status == updated_data.status

if __name__ == "__main__":
    pytest.main()
