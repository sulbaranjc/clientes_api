import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    def __init__(self) -> None:
        secret_key = os.getenv("SECRET_KEY")
        if not secret_key:
            raise RuntimeError("SECRET_KEY no está definida en el archivo .env")

        self.SECRET_KEY = secret_key
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
        )


settings = Settings()
