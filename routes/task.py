from fastapi import APIRouter
from app import cursor, conexao

router = APIRouter()

@router.post("/task", tags=["Task"])
def create_task(task: dict):
    cursor.execute('''INSERT INTO tasks (id, title, description, status) VALUES (?, ?, ?, ?)''',
                   (task["id"], task["title"], task["description"], task["status"]))
    conexao.commit()

    return {"message": "Successfully created task"}

@router.get("/task/{task_id}", tags=["Task"])
def get_task(task_id: int):
    cursor.execute('''SELECT * FROM tasks WHERE id = ?''', (task_id,))
    task = cursor.fetchone()
    if task:
        return {"Task": task}
    return {"Task": task}

@router.put("/task/{task_id}", tags=["Task"])
def update_task(task_id: int, updated_task: dict):
    cursor.execute('''UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?''',
                   (updated_task["title"], updated_task["description"], updated_task["status"], task_id))
    conexao.commit()
    return {"message": "Task updated successfully"}

@router.delete("/task/", tags=["Task"])
def delete_task(task_id:int):
    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
    conexao.commit()
    return {"message": "Task removed successfully"}