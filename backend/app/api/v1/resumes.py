from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    """Handles upload of resumes directly to R2 and runs Resume Analyzer."""
    return {"id": "mock-resume-id", "filename": file.filename}
