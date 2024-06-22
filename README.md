Tasks API
API para gerenciamento de tarefas utilizando FastAPI e SQLAlchemy.

Sugestão de estrutura:
fastapi-task-management/
project/
├── app/
│ ├── main.py
│ ├── config/
│ │ └── database.py
│ ├── controller/
│ │ └── task_controller.py
│ ├── domain/
│ │ │── dto/
│ │ | └── dtos.py
│ │ └── models.py  
│ ├── repository/
│ │ └── task_repository.py
│ ├── service/
│ │ └── task_service.py
│ └── database.db
└── tests/
└── test_task_controller.py

Descrição
Este projeto implementa uma API RESTful para gerenciar tarefas. As tarefas têm título, descrição, status e data de criação. Utiliza o FastAPI como framework web e o SQLAlchemy para interação com o banco de dados SQLite.

Funcionalidades
Criação de Tarefa: Endpoint para criar uma nova tarefa.
Atualização de Tarefa: Endpoint para atualizar uma tarefa existente.
Consulta de Tarefa por ID: Endpoint para obter detalhes de uma tarefa específica.
Listagem de Todas as Tarefas: Endpoint para listar todas as tarefas cadastradas.
Exclusão de Tarefa: Endpoint para excluir uma tarefa existente.
Pré-requisitos
Python 3.7 ou superior
Pip (gerenciador de pacotes do Python)
Instalação
Clone o repositório:
