from app import app
import sqlite3

@app.on_event("startup")
def startup():
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

    return conexao
