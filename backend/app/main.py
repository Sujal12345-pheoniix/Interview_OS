from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncGenerator

import sentry_sdk
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from app.core.config import settings
from app.core.database import engine
from app.core.redis_client import get_redis_client, close_redis
from app.core.qdrant_client import initialize_collections, close_qdrant


# ─── Lifespan ─────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """App startup and shutdown lifecycle"""
    logger.info(f"🚀 Starting {settings.APP_NAME} v{settings.APP_VERSION} [{settings.APP_ENV}]")

    # Initialize Redis
    try:
        redis = await get_redis_client()
        await redis.ping()
        logger.info("✅ Redis connected")
    except Exception as e:
        logger.error(f"❌ Redis connection failed: {e}")

    # Initialize Qdrant collections
    try:
        await initialize_collections()
        logger.info("✅ Qdrant initialized")
    except Exception as e:
        logger.warning(f"⚠️  Qdrant initialization failed: {e}")

    logger.info("✅ InterviewOS ready to serve requests")

    yield  # App is running

    # Shutdown
    logger.info("⏸️  Shutting down InterviewOS...")
    await close_redis()
    await close_qdrant()
    await engine.dispose()
    logger.info("✅ Shutdown complete")


# ─── Sentry ───────────────────────────────────────────────────────────────────

if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=settings.APP_ENV,
        traces_sample_rate=0.1,
        integrations=[
            FastApiIntegration(transaction_style="url"),
            SqlalchemyIntegration(),
        ],
    )
    logger.info("✅ Sentry initialized")


# ─── App Factory ──────────────────────────────────────────────────────────────

def create_app() -> FastAPI:
    app = FastAPI(
        title="InterviewOS API",
        description="AI-Powered Interview Operating System",
        version=settings.APP_VERSION,
        docs_url="/docs" if not settings.is_production else None,
        redoc_url="/redoc" if not settings.is_production else None,
        openapi_url="/openapi.json" if not settings.is_production else None,
        lifespan=lifespan,
    )

    # ── Middleware ──────────────────────────────────────────────
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Request-ID", "X-RateLimit-Remaining"],
    )

    # ── Exception Handlers ─────────────────────────────────────
    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"success": False, "message": str(exc), "data": None},
        )

    @app.exception_handler(PermissionError)
    async def permission_error_handler(request: Request, exc: PermissionError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"success": False, "message": str(exc), "data": None},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.error(f"Unhandled exception on {request.url}: {exc}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal server error",
                "data": None,
            },
        )

    # ── Routes ─────────────────────────────────────────────────
    from app.api.v1 import api_router
    app.include_router(api_router, prefix=f"/api/{settings.API_VERSION}")

    # ── Health Check ───────────────────────────────────────────
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {
            "status": "healthy",
            "app": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.APP_ENV,
        }

    @app.get("/", tags=["Root"])
    async def root():
        return {
            "message": f"Welcome to {settings.APP_NAME} API",
            "docs": "/docs",
            "version": settings.APP_VERSION,
        }

    return app


app = create_app()


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.is_development,
        workers=1 if settings.is_development else settings.WORKERS,
        log_level="debug" if settings.DEBUG else "info",
    )
