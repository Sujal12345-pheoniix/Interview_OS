from __future__ import annotations

import json
from loguru import logger

from app.agents.state import JDAnalysis
from app.services.llm_service import LLMService

JD_ANALYSIS_SYSTEM_PROMPT = """You are an expert technical recruiter and hiring manager.
Your task is to analyze the provided job description and extract requirements, key responsibilities, preferred skills, stack elements, and cultural signals.
Output your response in valid JSON matching this schema:
{
  "required_skills": ["skill1", "skill2"],
  "preferred_skills": ["skill3"],
  "responsibilities": ["resp1"],
  "requirements": ["req1"],
  "culture_signals": ["signal1"],
  "seniority_level": "junior|mid|senior|lead",
  "tech_stack": ["tech1"]
}
"""

JD_ANALYSIS_PROMPT = """Analyze the following Job Description text:

{jd_text}
"""


class JDAnalyzerAgent:
    """Agent 2: Parses job descriptions to identify key requirements and match signals."""

    def __init__(self):
        self.llm = LLMService()

    async def analyze(self, jd_text: str) -> JDAnalysis:
        logger.info("Analyzing job description...")
        try:
            response_text = await self.llm.generate(
                prompt=JD_ANALYSIS_PROMPT.format(jd_text=jd_text),
                system_prompt=JD_ANALYSIS_SYSTEM_PROMPT,
                temperature=0.2,
            )

            # Clean JSON
            clean_text = response_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            data = json.loads(clean_text)

            return JDAnalysis(
                required_skills=data.get("required_skills", []),
                preferred_skills=data.get("preferred_skills", []),
                responsibilities=data.get("responsibilities", []),
                requirements=data.get("requirements", []),
                culture_signals=data.get("culture_signals", []),
                seniority_level=data.get("seniority_level", "mid"),
                tech_stack=data.get("tech_stack", []),
                match_score=0.0,
            )
        except Exception as e:
            logger.error(f"Error parsing JD via LLM: {e}")
            return JDAnalysis()
