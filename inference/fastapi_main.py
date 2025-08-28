from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {"todo_id": 1, "todo_name": 'Read', "todo_description": "Read chip book"},
    {"todo_id": 2, "todo_name": 'code', "todo_description": "code fastapi"},
    {"todo_id": 3, "todo_name": 'Read', "todo_description": "Read blog"},
    {"todo_id": 4, "todo_name": 'Read', "todo_description": "Read Data intesive book"},
    {"todo_id": 5, "todo_name": 'code', "todo_description": "code llm training and fine tunning"},
    {"todo_id": 6, "todo_name": 'Relax', "todo_description": "Take a break and relax"},

]


@api.get('/')
def index():
    return {"message": "hello fastapi api server!"}


@api.get('/todos/{todo_id}')
def get_todo(todo_id):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}
        


@api.get('/todos')
def get_todos(todo_id):
    return all_todos
