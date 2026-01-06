from typing import Dict

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt import decode_access_token

# OAuth2 con Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict:
    """
    Extrae y valida el usuario actual desde el JWT.
    """
    try:
        payload = decode_access_token(token)
        username = payload.get("sub")
        role = payload.get("role")

        if not username or not role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        return {
            "username": username,
            "role": role
        }

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )


def require_admin(user: Dict = Depends(get_current_user)) -> Dict:
    """
    Verifica que el usuario tenga rol administrador.
    """
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permisos insuficientes"
        )
    return user
