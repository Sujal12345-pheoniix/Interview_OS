from __future__ import annotations

import contextlib
from typing import Any, Optional

import redis.asyncio as redis
from loguru import logger

from app.core.config import settings

# Global Redis client
_redis_client: Optional[redis.Redis] = None


async def get_redis_client() -> redis.Redis:
    """Get or create the global Redis client"""
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(
            settings.REDIS_URL,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis_client


async def close_redis() -> None:
    """Close the Redis connection pool"""
    global _redis_client
    if _redis_client:
        await _redis_client.aclose()
        _redis_client = None


# ─── Helper Functions ─────────────────────────────────────────────────────────

async def redis_get(key: str) -> Optional[str]:
    """Get a value from Redis"""
    client = await get_redis_client()
    return await client.get(key)


async def redis_set(key: str, value: str, expire: Optional[int] = None) -> None:
    """Set a value in Redis with optional expiry (seconds)"""
    client = await get_redis_client()
    if expire:
        await client.setex(key, expire, value)
    else:
        await client.set(key, value)


async def redis_delete(key: str) -> None:
    """Delete a key from Redis"""
    client = await get_redis_client()
    await client.delete(key)


async def redis_exists(key: str) -> bool:
    """Check if a key exists in Redis"""
    client = await get_redis_client()
    return bool(await client.exists(key))


async def redis_expire(key: str, seconds: int) -> None:
    """Set TTL on an existing key"""
    client = await get_redis_client()
    await client.expire(key, seconds)


async def redis_hset(key: str, mapping: dict[str, Any]) -> None:
    """Set hash fields in Redis"""
    client = await get_redis_client()
    await client.hset(key, mapping=mapping)


async def redis_hget(key: str, field: str) -> Optional[str]:
    """Get a hash field from Redis"""
    client = await get_redis_client()
    return await client.hget(key, field)


async def redis_hgetall(key: str) -> dict[str, str]:
    """Get all hash fields from Redis"""
    client = await get_redis_client()
    return await client.hgetall(key)


async def redis_incr(key: str, amount: int = 1) -> int:
    """Increment a counter in Redis"""
    client = await get_redis_client()
    return await client.incrby(key, amount)


async def redis_lpush(key: str, *values: str) -> None:
    """Push values to a Redis list"""
    client = await get_redis_client()
    await client.lpush(key, *values)


async def redis_lrange(key: str, start: int = 0, end: int = -1) -> list[str]:
    """Get range of values from a Redis list"""
    client = await get_redis_client()
    return await client.lrange(key, start, end)


# ─── Key Builders ─────────────────────────────────────────────────────────────

class RedisKeys:
    """Centralized Redis key patterns for InterviewOS"""

    @staticmethod
    def user_session(user_id: str) -> str:
        return f"session:user:{user_id}"

    @staticmethod
    def interview_state(interview_id: str) -> str:
        return f"interview:state:{interview_id}"

    @staticmethod
    def interview_transcript(interview_id: str) -> str:
        return f"interview:transcript:{interview_id}"

    @staticmethod
    def voice_session(interview_id: str) -> str:
        return f"voice:session:{interview_id}"

    @staticmethod
    def rate_limit(user_id: str, action: str) -> str:
        return f"ratelimit:{action}:{user_id}"

    @staticmethod
    def agent_progress(interview_id: str, agent_name: str) -> str:
        return f"agent:progress:{interview_id}:{agent_name}"

    @staticmethod
    def user_interviews_count(user_id: str, month: str) -> str:
        return f"user:interviews:count:{user_id}:{month}"

    @staticmethod
    def evaluation_job(interview_id: str) -> str:
        return f"evaluation:job:{interview_id}"

    @staticmethod
    def resume_analysis(resume_id: str) -> str:
        return f"resume:analysis:{resume_id}"


# ─── TTL Constants ────────────────────────────────────────────────────────────

class RedisTTL:
    """TTL values in seconds"""
    SESSION = 24 * 60 * 60          # 24 hours
    INTERVIEW_STATE = 2 * 60 * 60   # 2 hours
    VOICE_SESSION = 2 * 60 * 60     # 2 hours
    RATE_LIMIT = 60                 # 1 minute
    RATE_LIMIT_HOUR = 60 * 60      # 1 hour
    RESUME_ANALYSIS = 7 * 24 * 60 * 60  # 7 days
    AGENT_PROGRESS = 60 * 60       # 1 hour
    MONTHLY_COUNTER = 31 * 24 * 60 * 60  # 31 days
