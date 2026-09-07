from database import database


def criar_cliente(cliente):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
    """, (
        cliente["nome"],
        cliente["email"]
    ))

    conexao.commit()

    cliente_id = cursor.lastrowid

    conexao.close()

    return {
        "id": cliente_id,
        "nome": cliente["nome"],
        "email": cliente["email"]
    }


def listar_clientes():

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email
        FROM clientes
    """)

    clientes = cursor.fetchall()

    conexao.close()

    return [dict(cliente) for cliente in clientes]


def buscar_cliente(cliente_id):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email
        FROM clientes
        WHERE id = ?
    """, (cliente_id,))

    cliente = cursor.fetchone()

    conexao.close()

    if cliente is None:
        return None

    return dict(cliente)


def atualizar_cliente(cliente_id, dados):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email
        FROM clientes
        WHERE id = ?
    """, (cliente_id,))

    cliente = cursor.fetchone()

    if cliente is None:

        conexao.close()

        return None

    nome = dados.get("nome", cliente["nome"])
    email = dados.get("email", cliente["email"])

    cursor.execute("""
        UPDATE clientes
        SET nome = ?, email = ?
        WHERE id = ?
    """, (
        nome,
        email,
        cliente_id
    ))

    conexao.commit()

    conexao.close()

    return {
        "id": cliente_id,
        "nome": nome,
        "email": email
    }


def excluir_cliente(cliente_id):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id
        FROM clientes
        WHERE id = ?
    """, (cliente_id,))

    cliente = cursor.fetchone()

    if cliente is None:

        conexao.close()

        return False

    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
    """, (cliente_id,))

    conexao.commit()

    conexao.close()

    return True