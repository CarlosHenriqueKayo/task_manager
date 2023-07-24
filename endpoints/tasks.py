from app import cursor, conexao, startup, app
from fastapi import Depends
from fastapi import APIRouter

router = APIRouter

# Cadastro
@app.post("/task", tags=["Task"])
def create_task(task: dict):
    global conexao
    global cursor
    
    #Inserir a tarefa no banco de dados
    cursor.execute('''INSERT INTO tasks (id, title, description, status) VALUES (?, ?, ?, ?)''',
                   (task["id"], task["title"], task["description"], task["status"]))
    conexao.commit()
    return {"message": "Successfully registered task"}

# Obter pelo id
@app.get("/task/{task_id}", tags=["Task"])
def get_task(task_id: int):
    global cursor

    cursor.execute('''SELECT * FROM tasks WHERE id = ?''', (task_id,))
    task = cursor.fetchone()
    if task:
        return {"Task": task}
    return {"message": "Task not found"}

# Atualizar
@app.put("/task/{task_id}", tags=["Task"])
def update_task(task_id: int, updated_task: dict):
    global conexao
    global cursor

    cursor.execute('''UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?''',
                   (updated_task["title"], updated_task["description"], updated_task["status"], task_id))
    conexao.commit()
    return {"message": "Task updated successfully"}
# Excluir 
@app.delete("/task/", tags=["Task"])
def delete_task(task_id:int):
    global conexao
    global cursor

    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
    conexao.commit()
    return {"message": "Task removed successfully"}