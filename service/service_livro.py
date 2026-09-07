from database import database


def criar_livro(livro):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO livros (nome, preco)
        VALUES (?, ?)
    """, (
        livro["nome"],
        livro["preco"]
    ))

    conexao.commit()

    livro_id = cursor.lastrowid

    conexao.close()

    return {
        "id": livro_id,
        "nome": livro["nome"],
        "preco": livro["preco"]
    }


def listar_livros():

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, preco
        FROM livros
    """)

    livros = cursor.fetchall()

    conexao.close()

    return [dict(livro) for livro in livros]


def buscar_livro(livro_id):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, preco
        FROM livros
        WHERE id = ?
    """, (livro_id,))

    livro = cursor.fetchone()

    conexao.close()

    if livro is None:
        return None

    return dict(livro)


def atualizar_livro(livro_id, dados):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, preco
        FROM livros
        WHERE id = ?
    """, (livro_id,))

    livro = cursor.fetchone()

    if livro is None:

        conexao.close()

        return None

    nome = dados.get("nome", livro["nome"])
    preco = dados.get("preco", livro["preco"])

    cursor.execute("""
        UPDATE livros
        SET nome = ?, preco = ?
        WHERE id = ?
    """, (
        nome,
        preco,
        livro_id
    ))

    conexao.commit()

    conexao.close()

    return {
        "id": livro_id,
        "nome": nome,
        "preco": preco
    }


def excluir_livro(livro_id):

    conexao = database.conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id
        FROM livros
        WHERE id = ?
    """, (livro_id,))

    livro = cursor.fetchone()

    if livro is None:

        conexao.close()

        return False

    cursor.execute("""
        DELETE FROM livros
        WHERE id = ?
    """, (livro_id,))

    conexao.commit()

    conexao.close()

    return True