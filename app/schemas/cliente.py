# app/schemas/cliente.py

from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import re


# =========================
# Modelo base con validaciones (idéntico al monolito)
# =========================
class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    direccion: Optional[str] = None

    @field_validator("nombre", "apellido")
    @classmethod
    def validar_nombre_apellido(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("El campo no puede estar vacío")

        v = v.strip()

        if len(v) < 2:
            raise ValueError("Debe tener al menos 2 caracteres")

        if len(v) > 50:
            raise ValueError("No puede exceder 50 caracteres")

        # Solo letras, espacios, tildes y caracteres del español
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", v):
            raise ValueError("Solo se permiten letras y espacios")

        return v.title()

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v.strip() == "":
            return None

        v = v.strip()

        telefono_limpio = re.sub(r"[\s\-\(\)]", "", v)

        if not re.match(r"^\+?\d{7,15}$", telefono_limpio):
            raise ValueError(
                "Formato de teléfono inválido. Debe contener entre 7 y 15 dígitos"
            )

        return v

    @field_validator("direccion")
    @classmethod
    def validar_direccion(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v.strip() == "":
            return None

        v = v.strip()

        if len(v) > 200:
            raise ValueError("La dirección no puede exceder 200 caracteres")

        return v


# =========================
# Modelo para datos históricos (BD)
# 👉 sin validaciones estrictas
# =========================
class ClienteDB(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None


# =========================
# Modelo para creación (POST)
# =========================
class ClienteCreate(ClienteBase):
    pass


# =========================
# Modelo para actualización (PUT)
# =========================
class ClienteUpdate(ClienteBase):
    pass


# =========================
# Modelo de respuesta API
# =========================
class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True
