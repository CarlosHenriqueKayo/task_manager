from fastapi import Depends, FastAPI
import sqlite3
from routes.user import router as user_router
from routes.task import router as task_router

app = FastAPI()

# Registrar os endpoints
app.include_router(user_router)
app.include_router(task_router)

# Função para criar a conexão com o DB
def create_connection():
    global conexao
    global cursor
    
    conexao = sqlite3.connect('base.db')
    cursor = conexao.cursor()
    # Criar a tabela de tarefas se ela não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # Criar a tabela de usuários se ela não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password INTEGER
    )''')

# Inicializar a conexão com o DB
@app.on_event("startup")
def startup():
    create_connection()

# Fechar a conexão com o DB 
@app.on_event("shutdown")
def shutdown():
    conexao.close()


