from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.post("/")
async def create_interview(payload: dict, db: AsyncSession = Depends(get_db)):
    """Initialize a new mock interview session draft."""
    return {"id": "mock-interview-id", "status": "draft"}

@router.post("/{interview_id}/start")
async def start_interview(interview_id: str, db: AsyncSession = Depends(get_db)):
    """Start an interview session, compiling the questions."""
    return {"status": "in_progress", "websocket_url": "ws://localhost:8000/v1/voice/interview/" + interview_id}
