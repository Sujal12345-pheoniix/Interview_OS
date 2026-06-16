from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.get("/me")
async def get_current_user_profile(db: AsyncSession = Depends(get_db)):
    """Fetch current logged-in user profile details."""
    return {"id": "mock-user-id", "email": "candidate@example.com"}
