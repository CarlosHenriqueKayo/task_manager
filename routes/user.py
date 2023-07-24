from fastapi import APIRouter, Depends
from app import cursor, conexao

router = APIRouter()

# Cadastro 
@router.post("/user", tags= ["User"])
def create_user(user: dict):
    # Inserir usuario no db
    cursor.execute('''INSERT INTO users (id, name, email, password) VALUES (?, ?, ?, ?)''',
               (user ["id"], user["name"], user["email"], user["password"]))
    conexao.commit()

    return {"message": "User created successfully"}

# Obter pelo id
@router.get("/user/{user_id}", tags=["User"])
def get_user(user_id: int):
    cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
    user = cursor.fetchone()
    if user:
        return {"User": user}
    return {"message": "User not found"}

# Tarefa vinculada ao usuário pelo id
@router.get("/user/{user_id}/task", tags=["User"])
def get_user_task(user_id=int):
    cursor.execute('''SELECT * FROM tasks WHERE user_id = ?''', (user_id,))
    tasks = cursor.fetchall()
    return {"Tasks": tasks}

# Exluir pelo id
@router.delete("/user/{user_id}", tags=["User"])
def delete_user(user_id: int):
    cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    conexao.commit()
    return {"message": "User removed successfully"}
