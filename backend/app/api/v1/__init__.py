from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.resumes import router as resumes_router
from app.api.v1.interviews import router as interviews_router
from app.api.v1.voice import router as voice_router
from app.api.v1.reports import router as reports_router
from app.api.v1.analytics import router as analytics_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(resumes_router, prefix="/resumes", tags=["Resumes"])
api_router.include_router(interviews_router, prefix="/interviews", tags=["Interviews"])
api_router.include_router(voice_router, prefix="/voice", tags=["Voice"])
api_router.include_router(reports_router, prefix="/reports", tags=["Reports"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
