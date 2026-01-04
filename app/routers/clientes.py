# app/routers/clientes.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from mysql.connector import Error

from app.schemas.cliente import ClienteResponse
from app.database import get_all_clientes, get_cliente_by_id

from app.schemas.cliente import (
    ClienteResponse,
    ClienteCreate
)
from app.database import (
    get_all_clientes,
    get_cliente_by_id,
    create_cliente
)

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get("/", response_model=List[ClienteResponse])
def listar_clientes():
    return get_all_clientes()


@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener_cliente(cliente_id: int):
    cliente = get_cliente_by_id(cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return cliente

# =========================
# POST /clientes
# =========================
@router.post(
    "/",
    response_model=ClienteResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_cliente(cliente: ClienteCreate):
    try:
        nuevo_id = create_cliente(cliente.model_dump())

        cliente_creado = get_cliente_by_id(nuevo_id)
        return cliente_creado

    except Error as e:
        # MySQL error code 1062 = Duplicate entry (email UNIQUE)
        if e.errno == 1062:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un cliente con ese email"
            )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear el cliente"
        )