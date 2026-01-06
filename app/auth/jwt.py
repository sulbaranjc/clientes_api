from datetime import datetime, timedelta
from typing import Any, Dict

from jose import JWTError, jwt

from app.core.config import settings


def create_access_token(
    data: Dict[str, Any],
    expires_delta: timedelta | None = None
) -> str:
    """
    Crea un JWT firmado con fecha de expiración.
    """
    to_encode = data.copy()

    expire = (
        datetime.utcnow() + expires_delta
        if expires_delta
        else datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Decodifica y valida un JWT.
    Lanza excepción si es inválido o expiró.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError as exc:
        raise ValueError("Token inválido o expirado") from exc
