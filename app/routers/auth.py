# app/routers/auth.py
"""
Router de autenticación.

Implementa login mediante OAuth2 Password Flow
compatible con Swagger UI y JWT.
"""

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.passwords import verify_password
from app.auth.jwt import create_access_token
from app.repository.users_repo import get_user_by_username

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# ======================================================
# POST /auth/login
# ======================================================
@router.post(
    "/login",
    summary="Login y generación de JWT",
    description="""
    Autenticación de usuario usando **OAuth2 Password Flow**.

    - Compatible con Swagger UI (Authorize)
    - Devuelve un JWT Bearer
    - Usa username y password
    """,
)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Autentica un usuario y devuelve un access_token JWT.
    """

    # 1️⃣ Buscar usuario
    user = get_user_by_username(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2️⃣ Verificar password
    if not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3️⃣ Crear token
    access_token = create_access_token(
        data={
            "sub": user["username"],
            "role": user["role"]
        }
    )

    # 4️⃣ Respuesta estándar OAuth2
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
