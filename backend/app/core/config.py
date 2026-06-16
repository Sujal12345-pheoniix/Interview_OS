from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ─── App ──────────────────────────────────────────────────
    APP_NAME: str = "InterviewOS"
    APP_ENV: str = "development"
    APP_VERSION: str = "0.1.0"
    API_VERSION: str = "v1"
    DEBUG: bool = False
    SECRET_KEY: str = "change-me-in-production-use-strong-random-key"

    # ─── Server ───────────────────────────────────────────────
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    # ─── Database ─────────────────────────────────────────────
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/interviewos"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30
    DATABASE_POOL_TIMEOUT: int = 30
    DATABASE_POOL_RECYCLE: int = 3600

    @property
    def clean_database_url(self) -> str:
        url = self.DATABASE_URL.strip()
        # Fix double colon typo (e.g., postgresql+asyncpg:://)
        if "postgresql+asyncpg:://" in url:
            url = url.replace("postgresql+asyncpg:://", "postgresql+asyncpg://")
        elif "postgres:://" in url:
            url = url.replace("postgres:://", "postgresql+asyncpg://")
        # Fix standard postgres scheme to use asyncpg
        elif url.startswith("postgres://"):
            url = "postgresql+asyncpg://" + url[11:]
        elif url.startswith("postgresql://"):
            url = "postgresql+asyncpg://" + url[13:]
        return url

    @property
    def sync_database_url(self) -> str:
        """Returns synchronous DB URL for Alembic migrations"""
        return self.clean_database_url.replace("+asyncpg", "+psycopg2")

    # ─── Redis ────────────────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"
    UPSTASH_REDIS_REST_URL: Optional[str] = None
    UPSTASH_REDIS_REST_TOKEN: Optional[str] = None
    REDIS_MAX_CONNECTIONS: int = 50

    # ─── Qdrant ───────────────────────────────────────────────
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: Optional[str] = None
    QDRANT_RESUME_COLLECTION: str = "resumes"
    QDRANT_QUESTIONS_COLLECTION: str = "questions"
    EMBEDDING_DIMENSION: int = 384  # BGE-small

    # ─── AI / LLM ─────────────────────────────────────────────
    GEMINI_API_KEY: Optional[str] = None
    GEMINI_MODEL: str = "gemini-2.5-flash"
    GEMINI_MAX_TOKENS: int = 8192
    GEMINI_TEMPERATURE: float = 0.7

    OPENROUTER_API_KEY: Optional[str] = None
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL: str = "anthropic/claude-3.5-sonnet"

    OPENAI_API_KEY: Optional[str] = None

    LLM_MAX_RETRIES: int = 3
    LLM_RETRY_DELAY: float = 1.0

    # ─── Voice ────────────────────────────────────────────────
    DEEPGRAM_API_KEY: Optional[str] = None
    DEEPGRAM_MODEL: str = "nova-2"
    DEEPGRAM_LANGUAGE: str = "en-US"

    CARTESIA_API_KEY: Optional[str] = None
    CARTESIA_VOICE_ID: str = "a0e99841-438c-4a64-b679-ae501e7d6091"  # Sonic English
    CARTESIA_MODEL: str = "sonic-english"

    # ─── Auth (Clerk) ─────────────────────────────────────────
    CLERK_SECRET_KEY: Optional[str] = None
    CLERK_PUBLISHABLE_KEY: Optional[str] = None
    CLERK_WEBHOOK_SECRET: Optional[str] = None

    # ─── Storage (Cloudflare R2) ──────────────────────────────
    CLOUDFLARE_ACCOUNT_ID: Optional[str] = None
    CLOUDFLARE_R2_ACCESS_KEY: Optional[str] = None
    CLOUDFLARE_R2_SECRET_KEY: Optional[str] = None
    CLOUDFLARE_R2_BUCKET: str = "interviewos"

    @property
    def r2_endpoint_url(self) -> Optional[str]:
        if self.CLOUDFLARE_ACCOUNT_ID:
            return f"https://{self.CLOUDFLARE_ACCOUNT_ID}.r2.cloudflarestorage.com"
        return None

    # ─── Monitoring ───────────────────────────────────────────
    SENTRY_DSN: Optional[str] = None
    POSTHOG_API_KEY: Optional[str] = None
    POSTHOG_HOST: str = "https://app.posthog.com"

    # ─── Rate Limiting ────────────────────────────────────────
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_PER_HOUR: int = 1000

    # ─── Interview Limits ─────────────────────────────────────
    FREE_INTERVIEWS_PER_MONTH: int = 3
    PRO_INTERVIEWS_PER_MONTH: int = 999999  # Unlimited

    # ─── File Upload ──────────────────────────────────────────
    MAX_FILE_SIZE_MB: int = 10
    ALLOWED_RESUME_TYPES: list[str] = ["application/pdf", "application/msword",
                                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]

    @property
    def max_file_size_bytes(self) -> int:
        return self.MAX_FILE_SIZE_MB * 1024 * 1024

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"


# Global settings instance
settings = Settings()
