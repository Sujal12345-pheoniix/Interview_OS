from __future__ import annotations

import json
from typing import Any, Optional

from loguru import logger
from qdrant_client import AsyncQdrantClient
from qdrant_client.http import models as qmodels
from qdrant_client.http.exceptions import UnexpectedResponse

from app.core.config import settings

# Global Qdrant client
_qdrant_client: Optional[AsyncQdrantClient] = None


async def get_qdrant_client() -> AsyncQdrantClient:
    """Get or create the global Qdrant client"""
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = AsyncQdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            timeout=30,
        )
    return _qdrant_client


async def close_qdrant() -> None:
    """Close the Qdrant client"""
    global _qdrant_client
    if _qdrant_client:
        await _qdrant_client.close()
        _qdrant_client = None


async def initialize_collections() -> None:
    """Initialize Qdrant collections on startup"""
    client = await get_qdrant_client()

    collections_to_create = [
        {
            "name": settings.QDRANT_RESUME_COLLECTION,
            "description": "Resume embeddings for semantic search and matching",
        },
        {
            "name": settings.QDRANT_QUESTIONS_COLLECTION,
            "description": "Question embeddings for deduplication and search",
        },
    ]

    for collection_config in collections_to_create:
        collection_name = collection_config["name"]
        try:
            # Check if collection exists
            await client.get_collection(collection_name)
            logger.info(f"Qdrant collection '{collection_name}' already exists")
        except (UnexpectedResponse, Exception):
            # Create collection
            await client.create_collection(
                collection_name=collection_name,
                vectors_config=qmodels.VectorParams(
                    size=settings.EMBEDDING_DIMENSION,
                    distance=qmodels.Distance.COSINE,
                    on_disk=False,
                ),
                optimizers_config=qmodels.OptimizersConfigDiff(
                    default_segment_number=2,
                    memmap_threshold=20000,
                ),
                hnsw_config=qmodels.HnswConfigDiff(
                    m=16,
                    ef_construct=100,
                    full_scan_threshold=10000,
                ),
            )
            logger.info(f"Created Qdrant collection '{collection_name}'")


async def upsert_vector(
    collection_name: str,
    vector_id: str,
    vector: list[float],
    payload: dict[str, Any],
) -> None:
    """Upsert a single vector into Qdrant"""
    client = await get_qdrant_client()
    await client.upsert(
        collection_name=collection_name,
        points=[
            qmodels.PointStruct(
                id=vector_id,
                vector=vector,
                payload=payload,
            )
        ],
    )


async def search_similar(
    collection_name: str,
    query_vector: list[float],
    limit: int = 10,
    score_threshold: float = 0.7,
    filters: Optional[dict] = None,
) -> list[dict[str, Any]]:
    """Search for similar vectors in Qdrant"""
    client = await get_qdrant_client()

    query_filter = None
    if filters:
        conditions = [
            qmodels.FieldCondition(
                key=k,
                match=qmodels.MatchValue(value=v),
            )
            for k, v in filters.items()
        ]
        query_filter = qmodels.Filter(must=conditions)

    results = await client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=limit,
        score_threshold=score_threshold,
        query_filter=query_filter,
        with_payload=True,
    )

    return [
        {
            "id": str(result.id),
            "score": result.score,
            "payload": result.payload or {},
        }
        for result in results
    ]


async def delete_vector(collection_name: str, vector_id: str) -> None:
    """Delete a vector from Qdrant"""
    client = await get_qdrant_client()
    await client.delete(
        collection_name=collection_name,
        points_selector=qmodels.PointIdsList(points=[vector_id]),
    )


async def get_vector(collection_name: str, vector_id: str) -> Optional[dict[str, Any]]:
    """Get a single vector by ID"""
    client = await get_qdrant_client()
    results = await client.retrieve(
        collection_name=collection_name,
        ids=[vector_id],
        with_payload=True,
        with_vectors=True,
    )
    if results:
        point = results[0]
        return {
            "id": str(point.id),
            "vector": point.vector,
            "payload": point.payload or {},
        }
    return None
