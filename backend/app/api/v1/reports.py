from fastapi import APIRouter

router = APIRouter()

@router.get("/{interview_id}")
async def get_report(interview_id: str):
    """Retrieve post-interview evaluation report summary."""
    return {
        "overall_score": 88.0,
        "hiring_recommendation": "hire",
        "strengths": ["Excellent structure", "Fast FastAPI explanation"],
        "weaknesses": ["Filler words detected"],
        "improvement_plan": {"weeks": []}
    }
