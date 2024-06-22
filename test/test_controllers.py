import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
from config.database import get_db
from domain.dto.dtos import taskDTO, taskCreateDTO, taskUpdateDTO

@pytest.fixture(scope="module")
def test_client():
    """Fixture para obter um cliente de teste do FastAPI."""
    client = TestClient(app)
    yield client

def test_create_task(test_client: TestClient, db: Session):
    """Teste para o endpoint POST /tasks/"""
    task_data = {"title": "Teste de Tarefa", "description": "Testando a criação de tarefa"}

    response = test_client.post("/tasks/", json=task_data)

    assert response.status_code == 201
    created_task = response.json()
    assert created_task["title"] == task_data["title"]
    assert created_task["description"] == task_data["description"]

def test_get_task(test_client: TestClient, db: Session):
    """Teste para o endpoint GET /tasks/{task_id}"""
    task_id = 1

    response = test_client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    task = response.json()
    assert task["id"] == task_id


if __name__ == "__main__":
    pytest.main()
