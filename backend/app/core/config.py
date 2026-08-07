from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -----------------------------
    # Application
    # -----------------------------
    app_name: str = "ScriptPilot AI"
    app_version: str = "1.0.0"
    debug: bool = True

    # -----------------------------
    # PostgreSQL
    # -----------------------------
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    # -----------------------------
    # JWT (Future)
    # -----------------------------
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # -----------------------------
    # Gemini (Future)
    # -----------------------------
    gemini_api_key: str = ""

    # -----------------------------
    # Pydantic Settings
    # -----------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # -----------------------------
    # Computed Database URL
    # -----------------------------
    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()