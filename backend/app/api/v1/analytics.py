from fastapi import APIRouter

router = APIRouter()

@router.get("/progress")
async def get_progress_data():
    """Retrieve score progression records over past sessions."""
    return {
        "readiness_score": 85.0,
        "skill_velocity": 4.5,
        "history": []
    }
