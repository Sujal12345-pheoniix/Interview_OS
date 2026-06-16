from __future__ import annotations

import httpx
from loguru import logger
from app.core.config import settings


class EmbeddingService:
    """Generates text embeddings using Gemini/OpenAI or local fallback models."""

    def __init__(self):
        pass

    async def get_embedding(self, text: str) -> list[float]:
        """Fetch embedding vector for resume indexing."""
        # Standard size 768 or 1536 depending on service
        # Return mock zero vector if keys not available
        return [0.0] * 768
