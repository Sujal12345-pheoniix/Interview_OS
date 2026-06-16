from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.post("/webhook", status_code=status.HTTP_200_OK)
async def clerk_webhook(payload: dict, db: AsyncSession = Depends(get_db)):
    """Receives Clerk webhooks to keep users database synchronized."""
    # Process user.created / user.updated events
    return {"status": "success"}
