from app import cursor, conexao, startup, app
from fastapi import Depends

# Cadastro 
@app.post("/user", tags= ["User"])
def create_user(user: dict):
    global conexao
    global cursor

    # Inserir usuario no db
    cursor.execute('''INSERT INTO users (id, name, email, password) VALUES (?, ?, ?, ?)''',
               (user ["id"], user["name"], user["email"], user["password"]))
    conexao.commit()

    return {"message": "User created successfully"}

# Obter pelo id
@app.get("/user/{user_id}", tags=["User"])
def get_user(user_id: int):
    global cursor

    cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
    user = cursor.fetchone()
    if user:
        return {"User": user}
    return {"message": "User not found"}

# Tarefa vinculada ao usuário pelo id
@app.get("/user/{user_id}/task", tags=["User"])
def get_user_task(user_id=int):
    global cursor
    
    cursor.execute('''SELECT * FROM tasks WHERE user_id = ?''', (user_id,))
    tasks = cursor.fetchall()
    return {"Tasks": tasks}

# Exluir pelo id
@app.delete("/user/{user_id}", tags=["User"])
def delete_user(user_id: int):
    global conexao
    global cursor

    cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    conexao.commit()
    return {"message": "User removed successfully"}