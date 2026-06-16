from __future__ import annotations

from app.prompts.resume_prompts import (
    RESUME_EXTRACTION_SYSTEM_PROMPT,
    RESUME_EXTRACTION_PROMPT,
)
from app.prompts.interview_prompts import (
    INTERVIEW_CONDUCTOR_SYSTEM_PROMPT,
    QUESTION_GENERATION_PROMPT,
)
from app.prompts.evaluation_prompts import (
    RESPONSE_EVALUATION_PROMPT,
    FINAL_REPORT_PROMPT,
)

__all__ = [
    "RESUME_EXTRACTION_SYSTEM_PROMPT",
    "RESUME_EXTRACTION_PROMPT",
    "INTERVIEW_CONDUCTOR_SYSTEM_PROMPT",
    "QUESTION_GENERATION_PROMPT",
    "RESPONSE_EVALUATION_PROMPT",
    "FINAL_REPORT_PROMPT",
]
