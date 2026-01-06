from typing import Optional, Dict, Any, cast
from app.database import get_connection


def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    assert conn is not None, "No se pudo obtener conexión a la base de datos"

    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT u.username, u.password_hash, r.nombre AS role
        FROM usuarios u
        JOIN roles r ON u.rol_id = r.id
        WHERE u.username = %s AND u.activo = 1
    """

    cursor.execute(query, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user is None:
        return None

    # Normalizamos el tipo para el resto de la aplicación
    return cast(Dict[str, Any], user)
