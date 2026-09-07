import sqlite3


BANCO = "biblioteca.db"


def conectar():
    conexao = sqlite3.connect(BANCO)

    conexao.row_factory = sqlite3.Row

    return conexao


def criar_tabelas():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conexao.commit()

    conexao.close()