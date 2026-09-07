from fastapi import APIRouter, HTTPException

from service import service_cliente


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.post("")
def criar_cliente(cliente: dict):

    return service_cliente.criar_cliente(cliente)


@router.get("")
def listar_clientes():

    return service_cliente.listar_clientes()


@router.get("/{cliente_id}")
def buscar_cliente(cliente_id: int):

    cliente = service_cliente.buscar_cliente(cliente_id)

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente


@router.put("/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: dict):

    resultado = service_cliente.atualizar_cliente(
        cliente_id,
        cliente
    )

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return resultado


@router.delete("/{cliente_id}")
def excluir_cliente(cliente_id: int):

    resultado = service_cliente.excluir_cliente(cliente_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return {
        "mensagem": "Cliente excluído com sucesso"
    }