from __future__ import annotations

import json
from loguru import logger
from app.services.llm_service import LLMService
from app.prompts.evaluation_prompts import RESPONSE_EVALUATION_PROMPT


class EvaluatorAgents:
    """Agents 5, 6, and 7: Communication, Technical, and Behavioral Evaluators."""

    def __init__(self):
        self.llm = LLMService()

    async def evaluate_response(
        self,
        question_text: str,
        expected_answer: str,
        evaluation_rubric: dict,
        candidate_answer: str,
    ) -> dict:
        logger.info("Evaluating candidate response...")
        prompt = RESPONSE_EVALUATION_PROMPT.format(
            question_text=question_text,
            expected_answer=expected_answer,
            evaluation_rubric=json.dumps(evaluation_rubric),
            candidate_answer=candidate_answer,
        )

        try:
            response_text = await self.llm.generate(
                prompt=prompt,
                system_prompt="You are an expert evaluator. Output valid JSON matching the schema.",
                temperature=0.2,
            )

            clean_text = response_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            return json.loads(clean_text)
        except Exception as e:
            logger.error(f"Error evaluating response: {e}")
            return {
                "score": 70.0,
                "reasoning": "Fallback score due to evaluation failure.",
                "rubric_scores": {"clarity": 70},
            }
