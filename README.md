# Task Manager Graphql

## Descrição

Este é um projeto simples que utiliza Django com GraphQL para gerenciar tarefas. Projetado para ajudar a consolidar o conhecimento em GraphQL, do curso **Comunicação entre Sistemas** do Full Cycle.

## Funcionalidades

Neste projeto, você pode realizar as seguintes ações:

- Adicionar novas tarefas.
- Listar tarefas existentes.
- Marcar tarefas como concluídas.

## Pré-Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python
- Django
- Graphene-Django

## Configuração do Projeto e Execução com Ambiente Virtual (env)

Para executar a aplicação usando um ambiente virtual (env), siga estas etapas:

1. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/MarinaSpadetto/task_manager_graphql.git
   ```

2. Crie um ambiente virtual usando venv ou virtualenv:

   ```
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:

   No Windows:
    ```
    venv\Scripts\activate
    ```

   No macOS e Linux:
    ```
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

6. Crie um superusuário para acessar a interface administrativa:

   ```
   python manage.py createsuperuser
   ```

7. Inicie o servidor:

   ```
   python manage.py runserver
   ```

8. Acesse http://localhost:8000/admin/ para adicionar tarefas usando a interface administrativa.

9. Acesse http://localhost:8000/graphql/ para usar a API GraphQL para adicionar, listar e concluir tarefas.

## Exemplos de Consultas GraphQL

### Listar todas as tarefas

```
query {
  allTasks {
    id
    title
    completed
  }
}
```

### Adicionar uma nova tarefa

```
mutation {
  createTask(title: "Nova Tarefa", completed: true) {
    task {
      title
      completed
    }
  }
}
```

---

*Desenvolvido por Marina Spadetto*
