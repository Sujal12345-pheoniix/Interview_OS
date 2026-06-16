from __future__ import annotations

import json
from loguru import logger

from app.agents.state import ResumeAnalysis
from app.services.llm_service import LLMService
from app.prompts.resume_prompts import (
    RESUME_EXTRACTION_SYSTEM_PROMPT,
    RESUME_EXTRACTION_PROMPT,
)


class ResumeAnalyzerAgent:
    """Agent 1: Extracts skills, projects, and work experience from resumes."""

    def __init__(self):
        self.llm = LLMService()

    async def analyze(self, resume_text: str, target_role: str = "") -> ResumeAnalysis:
        logger.info("Analyzing resume text using LLM...")
        prompt = RESUME_EXTRACTION_PROMPT.format(
            resume_text=resume_text,
            target_role=target_role,
            years_experience_claimed="unknown",
        )

        try:
            response_text = await self.llm.generate(
                prompt=prompt,
                system_prompt=RESUME_EXTRACTION_SYSTEM_PROMPT,
                temperature=0.2,
            )

            # Clean JSON if wrapped in markdown code blocks
            clean_text = response_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            data = json.loads(clean_text)

            return ResumeAnalysis(
                skills=data.get("skills", []),
                technical_skills=data.get("technical_skills", []),
                soft_skills=data.get("soft_skills", []),
                projects=data.get("projects", []),
                experience=data.get("experience", []),
                education=data.get("education", []),
                certifications=data.get("certifications", []),
                gaps=data.get("gaps", []),
                strengths=data.get("strengths", []),
                years_experience=data.get("years_experience", 0),
                seniority_level=data.get("seniority_level", "mid"),
            )
        except Exception as e:
            logger.error(f"Error parsing resume via LLM: {e}")
            # Fallback mock analysis
            return ResumeAnalysis(
                skills=["Python", "FastAPI", "SQLAlchemy"],
                technical_skills=["Python", "FastAPI"],
                soft_skills=["Communication"],
                years_experience=2,
            )
Def analyze_sync(self, resume_text: str, target_role: str = "") -> ResumeAnalysis:
        import asyncio
        return asyncio.run(self.analyze(resume_text, target_role))
