from passlib.context import CryptContext

# Contexto de hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Recibe una contraseña en texto plano
    y devuelve su hash seguro.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano
    coincide con su hash almacenado.
    """
    return pwd_context.verify(plain_password, hashed_password)
