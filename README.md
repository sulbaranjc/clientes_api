JC
# 🚀 API REST de Gestión de Clientes - Backend con FastAPI

## 📋 Tabla de Contenidos
1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Objetivos Pedagógicos](#-objetivos-pedagógicos)
3. [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
4. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
5. [Estructura del Proyecto](#-estructura-del-proyecto)
6. [Conceptos Clave](#-conceptos-clave)
7. [Requisitos Previos](#-requisitos-previos)
8. [Instalación y Configuración](#-instalación-y-configuración)
9. [Ejecución del Proyecto](#-ejecución-del-proyecto)
10. [API Endpoints](#-api-endpoints)
11. [Validaciones Implementadas](#-validaciones-implementadas)
12. [Manejo de Errores](#-manejo-de-errores)
13. [Buenas Prácticas Aplicadas](#-buenas-prácticas-aplicadas)
14. [Ejercicios Propuestos](#-ejercicios-propuestos)
15. [Recursos Adicionales](#-recursos-adicionales)

---

## 📖 Descripción del Proyecto

Este proyecto es una **API REST** desarrollada con **FastAPI** para la gestión de clientes. Forma parte de una arquitectura de aplicación moderna separando el backend del frontend, siguiendo el patrón de arquitectura de microservicios.

### 🎯 Finalidad Educativa

Este proyecto está diseñado específicamente para estudiantes de **Desarrollo de Aplicaciones Web** y **Desarrollo de Aplicaciones Multiplataforma**, con el objetivo de:

- Comprender la arquitectura de aplicaciones modernas (Backend separado del Frontend)
- Aprender a desarrollar APIs REST profesionales
- Implementar operaciones CRUD completas
- Aplicar validaciones de datos robustas
- Manejar errores de forma profesional
- Conectar aplicaciones Python con bases de datos MySQL

---

## 🎓 Objetivos Pedagógicos

Al finalizar el estudio de este proyecto, los alumnos serán capaces de:

1. **Comprender arquitecturas modernas**: Diferenciar entre arquitecturas monolíticas y basadas en APIs
2. **Desarrollar APIs REST**: Crear endpoints siguiendo las convenciones HTTP
3. **Implementar validaciones**: Asegurar la integridad de los datos mediante Pydantic
4. **Gestionar bases de datos**: Conectar y operar con MySQL desde Python
5. **Manejar errores**: Implementar respuestas HTTP apropiadas para diferentes situaciones
6. **Documentar automáticamente**: Aprovechar las capacidades de FastAPI para documentación interactiva
7. **Aplicar buenas prácticas**: Organizar código de forma modular y mantenible

---

## 🏗️ Arquitectura del Proyecto

Este proyecto implementa una **arquitectura en capas** (Layered Architecture):

```
┌─────────────────────────────────────┐
│      CLIENTE (Frontend)             │
│   (React, Vue, Angular, etc.)       │
└─────────────┬───────────────────────┘
              │ HTTP/JSON
              ↓
┌─────────────────────────────────────┐
│      CAPA DE PRESENTACIÓN           │
│     (Routers - Endpoints)           │
│  • GET /clientes                    │
│  • POST /clientes                   │
│  • PUT /clientes/{id}               │
│  • DELETE /clientes/{id}            │
└─────────────┬───────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│      CAPA DE VALIDACIÓN             │
│    (Schemas - Pydantic Models)      │
│  • ClienteCreate                    │
│  • ClienteUpdate                    │
│  • ClienteResponse                  │
└─────────────┬───────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│      CAPA DE LÓGICA                 │
│    (Database Functions)             │
│  • get_all_clientes()               │
│  • create_cliente()                 │
│  • update_cliente()                 │
│  • delete_cliente()                 │
└─────────────┬───────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│      CAPA DE DATOS                  │
│        (MySQL Database)             │
│     Tabla: clientes                 │
└─────────────────────────────────────┘
```

### Ventajas de esta Arquitectura:

- ✅ **Separación de responsabilidades**: Cada capa tiene una función específica
- ✅ **Mantenibilidad**: Fácil de modificar y extender
- ✅ **Reutilización**: El backend puede servir múltiples frontends
- ✅ **Escalabilidad**: Se puede escalar cada capa independientemente
- ✅ **Testabilidad**: Cada capa se puede probar de forma aislada

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| **Python** | 3.12+ | Lenguaje de programación principal |
| **FastAPI** | 0.128.0 | Framework web moderno para crear APIs |
| **Pydantic** | 2.12.5 | Validación de datos y serialización |
| **MySQL Connector** | 9.5.0 | Conexión con base de datos MySQL |
| **Uvicorn** | 0.40.0 | Servidor ASGI para ejecutar FastAPI |
| **Python-dotenv** | 1.2.1 | Gestión de variables de entorno |
| **Email-validator** | 2.3.0 | Validación de direcciones de email |

---

## 📁 Estructura del Proyecto

```
clientes_api/
│
├── app/                          # Paquete principal de la aplicación
│   ├── __init__.py              # Inicializa el paquete
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── database.py              # Funciones de acceso a datos
│   │
│   ├── routers/                 # Módulo de rutas/endpoints
│   │   ├── __init__.py
│   │   └── clientes.py          # Endpoints de gestión de clientes
│   │
│   └── schemas/                 # Módulo de modelos de datos
│       ├── __init__.py
│       └── cliente.py           # Modelos Pydantic para clientes
│
├── docs/                         # Documentación y scripts SQL
│   └── init_db.sql              # Script de inicialización de BD
│
├── .env                         # Variables de entorno (NO versionar)
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

### Descripción de Archivos Clave:

#### 📄 `app/main.py`
Archivo principal que:
- Inicializa la aplicación FastAPI
- Configura CORS para permitir peticiones desde el frontend
- Registra los routers (endpoints)
- Define el endpoint raíz

#### 📄 `app/database.py`
Contiene las funciones de acceso a datos:
- `get_connection()`: Establece conexión con MySQL
- `get_all_clientes()`: Obtiene todos los clientes
- `get_cliente_by_id()`: Obtiene un cliente por ID
- `create_cliente()`: Inserta un nuevo cliente
- `update_cliente()`: Actualiza un cliente existente
- `delete_cliente()`: Elimina un cliente

#### 📄 `app/routers/clientes.py`
Define los endpoints de la API:
- `GET /clientes`: Listar todos los clientes
- `GET /clientes/{id}`: Obtener un cliente específico
- `POST /clientes`: Crear un nuevo cliente
- `PUT /clientes/{id}`: Actualizar un cliente
- `DELETE /clientes/{id}`: Eliminar un cliente

#### 📄 `app/schemas/cliente.py`
Define los modelos de datos con Pydantic:
- `ClienteBase`: Modelo base con validaciones comunes
- `ClienteCreate`: Para crear nuevos clientes
- `ClienteUpdate`: Para actualizar clientes existentes
- `ClienteResponse`: Para las respuestas de la API
- `ClienteDB`: Representa los datos almacenados en BD

---

## 💡 Conceptos Clave

### 1️⃣ API REST
**REST** (Representational State Transfer) es un estilo de arquitectura que utiliza HTTP para la comunicación entre cliente y servidor.

**Características:**
- Usa métodos HTTP estándar (GET, POST, PUT, DELETE)
- Recursos identificados por URLs
- Sin estado (stateless)
- Formato JSON para intercambio de datos

### 2️⃣ CRUD Operations
**CRUD** = Create, Read, Update, Delete

| Operación | Método HTTP | Endpoint | Descripción |
|-----------|-------------|----------|-------------|
| **Create** | POST | `/clientes` | Crear nuevo cliente |
| **Read** | GET | `/clientes` | Listar todos los clientes |
| **Read** | GET | `/clientes/{id}` | Obtener un cliente |
| **Update** | PUT | `/clientes/{id}` | Actualizar cliente |
| **Delete** | DELETE | `/clientes/{id}` | Eliminar cliente |

### 3️⃣ Códigos de Estado HTTP

| Código | Significado | Uso en el Proyecto |
|--------|-------------|-------------------|
| **200** | OK | Respuesta exitosa (GET, PUT) |
| **201** | Created | Cliente creado exitosamente |
| **204** | No Content | Cliente eliminado (sin contenido) |
| **404** | Not Found | Cliente no encontrado |
| **409** | Conflict | Email duplicado |
| **422** | Unprocessable Entity | Error de validación |
| **500** | Internal Server Error | Error del servidor |

### 4️⃣ Pydantic Models
Pydantic es una librería para validación de datos usando type hints de Python.

**Ventajas:**
- Validación automática de tipos
- Mensajes de error descriptivos
- Conversión automática de datos
- Documentación automática en Swagger

### 5️⃣ Dependency Injection
FastAPI usa inyección de dependencias para:
- Conexiones a base de datos
- Autenticación
- Validaciones comunes

### 6️⃣ CORS (Cross-Origin Resource Sharing)
Permite que el frontend (en otro dominio/puerto) pueda hacer peticiones a la API.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción: especificar dominios
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📋 Requisitos Previos

### Software Necesario:

1. **Python 3.12 o superior**
   ```bash
   python --version
   ```

2. **MySQL Server 8.0 o superior**
   ```bash
   mysql --version
   ```

3. **pip** (gestor de paquetes de Python)
   ```bash
   pip --version
   ```

4. **Editor de código** (recomendado: VS Code, PyCharm)

5. **Cliente de pruebas de API** (opcionales):
   - Postman
   - Insomnia
   - Thunder Client (extensión VS Code)

### Conocimientos Requeridos:

- ✅ Fundamentos de Python
- ✅ Conceptos básicos de SQL
- ✅ Protocolo HTTP
- ✅ JSON
- ✅ Línea de comandos básica

---

## ⚙️ Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si usas Git
git clone <url-del-repositorio>
cd clientes_api

# O descargar y extraer el ZIP
```

### Paso 2: Crear Entorno Virtual

**¿Por qué un entorno virtual?**
- Aísla las dependencias del proyecto
- Evita conflictos entre versiones
- Facilita la gestión de paquetes

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Base de Datos

#### 4.1 Crear la Base de Datos

```bash
# Ejecutar MySQL
mysql -u root -p

# Ejecutar el script de inicialización
source docs/init_db.sql

# O copiar y pegar el contenido del archivo
```

Esto creará:
- Base de datos `clientes_db`
- Tabla `clientes` con su estructura
- 5 registros de ejemplo

#### 4.2 Configurar Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
DB_NAME=clientes_db
```

⚠️ **IMPORTANTE**: Nunca subir el archivo `.env` a repositorios públicos (agregar a `.gitignore`)

### Paso 5: Verificar Instalación

```bash
# Ver paquetes instalados
pip list

# Verificar conexión a la BD (opcional)
python -c "from app.database import get_connection; print('OK' if get_connection() else 'ERROR')"
```

---

## ▶️ Ejecución del Proyecto

### Modo Desarrollo

```bash
# Asegúrate de estar en el directorio del proyecto
# y tener el entorno virtual activado

uvicorn app.main:app --reload
```

**Parámetros:**
- `app.main:app`: Indica el módulo y la instancia de FastAPI
- `--reload`: Recarga automáticamente al detectar cambios (solo desarrollo)

### Salida Esperada:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Acceder a la Aplicación:

| URL | Descripción |
|-----|-------------|
| http://127.0.0.1:8000 | Endpoint raíz |
| http://127.0.0.1:8000/docs | **Swagger UI** - Documentación interactiva |
| http://127.0.0.1:8000/redoc | **ReDoc** - Documentación alternativa |

### Modo Producción

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Parámetros adicionales:**
- `--host 0.0.0.0`: Acepta conexiones externas
- `--port 8000`: Puerto de escucha
- `--workers 4`: Número de procesos worker

---

## 🌐 API Endpoints

### 1️⃣ Listar Todos los Clientes

```http
GET /clientes
```

**Respuesta Exitosa (200):**
```json
[
  {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@example.com",
    "telefono": "555-0101",
    "direccion": "Calle 123, Ciudad"
  },
  ...
]
```

### 2️⃣ Obtener Un Cliente Específico

```http
GET /clientes/{id}
```

**Parámetros:**
- `id` (path): ID del cliente

**Respuesta Exitosa (200):**
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan.perez@example.com",
  "telefono": "555-0101",
  "direccion": "Calle 123, Ciudad"
}
```

**Respuesta Error (404):**
```json
{
  "detail": "Cliente no encontrado"
}
```

### 3️⃣ Crear Nuevo Cliente

```http
POST /clientes
Content-Type: application/json
```

**Cuerpo de la Petición:**
```json
{
  "nombre": "Pedro",
  "apellido": "González",
  "email": "pedro.gonzalez@example.com",
  "telefono": "+34 612345678",
  "direccion": "Av. Principal 456"
}
```

**Campos Obligatorios:**
- `nombre` ✅
- `apellido` ✅
- `email` ✅

**Campos Opcionales:**
- `telefono` (puede ser `null` o vacío)
- `direccion` (puede ser `null` o vacío)

**Respuesta Exitosa (201):**
```json
{
  "id": 6,
  "nombre": "Pedro",
  "apellido": "González",
  "email": "pedro.gonzalez@example.com",
  "telefono": "+34 612345678",
  "direccion": "Av. Principal 456"
}
```

**Respuesta Error - Email Duplicado (409):**
```json
{
  "detail": "Ya existe un cliente con ese email"
}
```

**Respuesta Error - Validación (422):**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "nombre"],
      "msg": "Debe tener al menos 2 caracteres"
    }
  ]
}
```

### 4️⃣ Actualizar Cliente

```http
PUT /clientes/{id}
Content-Type: application/json
```

**Parámetros:**
- `id` (path): ID del cliente a actualizar

**Cuerpo de la Petición:**
```json
{
  "nombre": "Pedro",
  "apellido": "González Sánchez",
  "email": "pedro.gonzalez@example.com",
  "telefono": "+34 687654321",
  "direccion": "Nueva Dirección 789"
}
```

**Respuesta Exitosa (200):**
```json
{
  "id": 6,
  "nombre": "Pedro",
  "apellido": "González Sánchez",
  "email": "pedro.gonzalez@example.com",
  "telefono": "+34 687654321",
  "direccion": "Nueva Dirección 789"
}
```

### 5️⃣ Eliminar Cliente

```http
DELETE /clientes/{id}
```

**Parámetros:**
- `id` (path): ID del cliente a eliminar

**Respuesta Exitosa (204):**
Sin contenido

**Respuesta Error (404):**
```json
{
  "detail": "Cliente no encontrado"
}
```

---

## ✅ Validaciones Implementadas

### Campo: `nombre` y `apellido`

| Regla | Descripción | Ejemplo Válido | Ejemplo Inválido |
|-------|-------------|----------------|------------------|
| **No vacío** | No puede estar vacío | "Juan" | "" o "   " |
| **Longitud mínima** | Al menos 2 caracteres | "Li" | "J" |
| **Longitud máxima** | Máximo 50 caracteres | "Juan Carlos" | (Cadena > 50) |
| **Solo letras** | Letras, espacios y acentos | "José María" | "Juan123" |
| **Capitalización** | Convierte a Title Case | "JUAN" → "Juan" | - |

### Campo: `email`

| Regla | Descripción | Ejemplo Válido | Ejemplo Inválido |
|-------|-------------|----------------|------------------|
| **Formato válido** | Email bien formado | "user@example.com" | "user@" o "user.com" |
| **Único en BD** | No puede repetirse | "nuevo@example.com" | (Email existente) |

### Campo: `telefono` (opcional)

| Regla | Descripción | Ejemplo Válido | Ejemplo Inválido |
|-------|-------------|----------------|------------------|
| **Formato** | 7-15 dígitos | "+34 612345678" | "123" |
| **Caracteres permitidos** | Números, +, -, (), espacios | "555-0101" | "abc123" |
| **Limpieza** | Elimina espacios y guiones | "555 - 0101" → validado | - |

### Campo: `direccion` (opcional)

| Regla | Descripción | Ejemplo Válido | Ejemplo Inválido |
|-------|-------------|----------------|------------------|
| **Longitud máxima** | Máximo 200 caracteres | "Calle 123, Piso 4" | (Cadena > 200) |

### Validaciones a Nivel de Base de Datos

```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,           -- No nulo
    apellido VARCHAR(100) NOT NULL,         -- No nulo
    email VARCHAR(150) NOT NULL UNIQUE,     -- No nulo y único
    telefono VARCHAR(50),                   -- Opcional
    direccion VARCHAR(255)                  -- Opcional
);
```

---

## 🚨 Manejo de Errores

### Estrategia de Manejo de Errores

El proyecto implementa un manejo robusto de errores en múltiples niveles:

#### 1️⃣ Errores de Validación (422)

FastAPI + Pydantic validan automáticamente:
- Tipos de datos incorrectos
- Campos requeridos faltantes
- Formatos inválidos

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "nombre"],
      "msg": "Debe tener al menos 2 caracteres",
      "input": "J"
    }
  ]
}
```

#### 2️⃣ Errores de Negocio

**Cliente no encontrado (404):**
```python
if not cliente:
    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )
```

**Email duplicado (409):**
```python
if e.errno == 1062:  # MySQL duplicate entry
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Ya existe un cliente con ese email"
    )
```

#### 3️⃣ Errores de Conexión (500)

```python
def get_connection():
    try:
        connection = mysql.connector.connect(...)
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
```

### Tabla de Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| **ConnectionError** | No se puede conectar a MySQL | Verificar servicio MySQL, credenciales en `.env` |
| **404 Not Found** | ID de cliente inexistente | Verificar que el ID existe en la BD |
| **409 Conflict** | Email ya registrado | Usar un email diferente |
| **422 Validation Error** | Datos inválidos en el body | Revisar formato y campos requeridos |
| **500 Internal Server** | Error en el servidor | Revisar logs de Uvicorn |

---

## 🏆 Buenas Prácticas Aplicadas

### 1️⃣ Organización del Código

✅ **Separación por responsabilidades:**
- Routers → Endpoints
- Schemas → Validaciones
- Database → Acceso a datos

### 2️⃣ Nomenclatura

✅ **Convenciones Python (PEP 8):**
- `snake_case` para funciones y variables
- `PascalCase` para clases
- Nombres descriptivos

```python
# ✅ Correcto
def get_cliente_by_id(cliente_id: int):
    ...

# ❌ Incorrecto
def getClient(id):
    ...
```

### 3️⃣ Type Hints

✅ **Uso de anotaciones de tipo:**

```python
def create_cliente(data: dict) -> int:
    ...
```

### 4️⃣ Validación de Datos

✅ **Validaciones exhaustivas con Pydantic**
✅ **Mensajes de error descriptivos**

### 5️⃣ Seguridad

✅ **Variables de entorno** para credenciales
✅ **Prepared statements** (protección contra SQL injection)
✅ **Validación de email único**

```python
# ✅ Prepared statement
cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))

# ❌ Concatenación (vulnerable a SQL injection)
cursor.execute(f"SELECT * FROM clientes WHERE id = {cliente_id}")
```

### 6️⃣ Documentación

✅ **Comentarios explicativos**
✅ **Docstrings** (cuando es necesario)
✅ **Documentación automática** (Swagger/OpenAPI)

### 7️⃣ Manejo de Recursos

✅ **Cerrar conexiones:**

```python
cursor.close()
conn.close()
```

### 8️⃣ Códigos HTTP Apropiados

✅ **200** para GET/PUT exitosos
✅ **201** para POST exitosos
✅ **204** para DELETE exitosos
✅ **404** para recursos no encontrados
✅ **409** para conflictos

---

## 🎯 Ejercicios Propuestos

### Nivel Básico

1. **Agregar un nuevo campo:**
   - Añadir campo `fecha_nacimiento` a la tabla y modelo
   - Implementar validación (mayor de 18 años)

2. **Endpoint de búsqueda:**
   - Crear `GET /clientes/buscar?email=...`
   - Buscar cliente por email

3. **Paginación:**
   - Modificar `GET /clientes` para aceptar parámetros `limit` y `offset`
   - Implementar paginación en la consulta SQL

### Nivel Intermedio

4. **Endpoint de estadísticas:**
   - Crear `GET /clientes/estadisticas`
   - Retornar: total de clientes, clientes por dominio de email, etc.

5. **Soft Delete:**
   - Agregar campo `activo` (boolean)
   - Modificar DELETE para marcar como inactivo en vez de eliminar
   - Filtrar clientes inactivos en GET

6. **Logging:**
   - Implementar logging con el módulo `logging`
   - Registrar todas las operaciones CRUD

### Nivel Avanzado

7. **Autenticación:**
   - Agregar JWT authentication
   - Proteger endpoints (excepto GET)

8. **Testing:**
   - Escribir tests unitarios con `pytest`
   - Tests de integración para los endpoints

9. **Segunda entidad:**
   - Crear entidad `Pedidos`
   - Relación: Un cliente tiene muchos pedidos
   - Implementar CRUD completo

10. **Migraciones:**
    - Usar `Alembic` para gestionar cambios en la BD
    - Crear script de migración para agregar nuevo campo

---

## 📚 Recursos Adicionales

### Documentación Oficial

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### Tutoriales y Guías

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Real Python - FastAPI](https://realpython.com/fastapi-python-web-apis/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [REST API Design](https://restfulapi.net/)

### Herramientas Recomendadas

- **Postman**: Testing de APIs
- **DBeaver**: Cliente de bases de datos
- **VS Code Extensions**:
  - Python
  - Pylance
  - Thunder Client
  - MySQL

### Videos Educativos

- [Curso FastAPI (YouTube)](https://www.youtube.com/results?search_query=fastapi+tutorial+español)
- [REST API Concepts](https://www.youtube.com/results?search_query=rest+api+concepts)

---

## 🤝 Contribuciones

Este proyecto es educativo. Se anima a los estudiantes a:

- Reportar bugs
- Proponer mejoras
- Hacer fork y experimentar
- Compartir aprendizajes

---

## 📝 Licencia

Este proyecto es de uso educativo y libre distribución.

---

## ✉️ Contacto

**Autor:** Juan Carlos Sulbarán González  
**Propósito:** Material educativo para DAW/DAM  
**Fecha:** 2025

---

## 🙏 Agradecimientos

A todos los estudiantes que utilicen este proyecto como recurso de aprendizaje. ¡Mucho éxito en su formación como desarrolladores!

---

**¡Happy Coding! 🚀**
