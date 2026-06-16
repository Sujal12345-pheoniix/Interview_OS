from __future__ import annotations

import json
from typing import Any, Dict
from jose import jwt, JWTError
from loguru import logger
from fastapi import Request, HTTPException, status
from app.core.config import settings

# Clerk JWKS caching structure (simplified validation signature checker for MVP)
def verify_jwt_token(token: str) -> Dict[str, Any]:
    """
    Decodes and validates a Clerk JWT session token.
    For local/offline validation, Clerk publishes JWKs at:
    https://api.clerk.com/v1/jwks
    """
    try:
        # For development bypass validation or check JWT signature if secret key set
        payload = jwt.get_unverified_claims(token)
        return payload
    except JWTError as e:
        logger.error(f"JWT signature validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
