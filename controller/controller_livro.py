from fastapi import APIRouter, HTTPException

from service import service_livro


router = APIRouter(
    prefix="/livros",
    tags=["Livros"]
)


@router.post("")
def criar_livro(livro: dict):

    return service_livro.criar_livro(livro)


@router.get("")
def listar_livros():

    return service_livro.listar_livros()


@router.get("/{livro_id}")
def buscar_livro(livro_id: int):

    livro = service_livro.buscar_livro(livro_id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro


@router.put("/{livro_id}")
def atualizar_livro(livro_id: int, livro: dict):

    resultado = service_livro.atualizar_livro(
        livro_id,
        livro
    )

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return resultado


@router.delete("/{livro_id}")
def excluir_livro(livro_id: int):

    resultado = service_livro.excluir_livro(livro_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return {
        "mensagem": "Livro excluído com sucesso"
    }