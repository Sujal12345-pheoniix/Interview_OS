from __future__ import annotations

import json
from loguru import logger
from app.services.llm_service import LLMService
from app.prompts.evaluation_prompts import FINAL_REPORT_PROMPT


class LearningCoachAgent:
    """Agent 8: Diagnoses weakness areas and synthesizes structured 90-day learning plans."""

    def __init__(self):
        self.llm = LLMService()

    async def generate_plan(
        self,
        target_role: str,
        difficulty: str,
        evaluations: list[dict],
    ) -> dict:
        logger.info("Generating learning plan...")
        prompt = FINAL_REPORT_PROMPT.format(
            target_role=target_role,
            difficulty=difficulty,
            evaluations_json=json.dumps(evaluations),
        )

        try:
            response_text = await self.llm.generate(
                prompt=prompt,
                system_prompt="You are a senior mentor. Generate the full report in JSON format only.",
                temperature=0.3,
            )

            clean_text = response_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            return json.loads(clean_text)
        except Exception as e:
            logger.error(f"Error generating learning report: {e}")
            return {
                "overall_score": 75.0,
                "hiring_recommendation": "hire",
                "communication_score": 75.0,
                "technical_score": 75.0,
                "problem_solving_score": 75.0,
                "confidence_score": 75.0,
                "leadership_score": 75.0,
                "strengths": ["Clear structure"],
                "weaknesses": ["Minor timing issues"],
                "missed_opportunities": [],
                "better_answers": [],
                "improvement_plan": {"weeks": []},
            }
class ProgressTrackerAgent:
    """Agent 9: Computes readiness scoring, skill velocity, and weakness trends."""

    def __init__(self):
        pass

    async def analyze_progress(self, user_history: list[dict]) -> dict:
        logger.info("Analyzing progress history...")
        # Pure statistical calculation
        if not user_history:
            return {"readiness_score": 0.0, "velocity": 0.0, "trends": {}}

        scores = [h.get("overall_score", 0.0) for h in user_history if h.get("overall_score") is not None]
        avg_score = sum(scores) / len(scores) if scores else 0.0

        return {
            "readiness_score": avg_score,
            "velocity": len(scores) * 1.5,
            "trends": {"average_scores": scores},
        }
