from __future__ import annotations

import json
from loguru import logger

from app.agents.state import GeneratedQuestion, ResumeAnalysis, JDAnalysis
from app.services.llm_service import LLMService
from app.prompts.interview_prompts import QUESTION_GENERATION_PROMPT


class QuestionGeneratorAgent:
    """Agent 3: Generates customized questions tailored to resume + JD + role."""

    def __init__(self):
        self.llm = LLMService()

    async def generate(
        self,
        interview_type: str,
        interview_subtype: str,
        difficulty: str,
        target_role: str,
        resume: Optional[ResumeAnalysis] = None,
        jd: Optional[JDAnalysis] = None,
        num_questions: int = 5,
    ) -> list[GeneratedQuestion]:
        logger.info("Generating customized questions...")

        resume_context = json.dumps(resume.__dict__) if resume else "No resume provided."
        jd_context = json.dumps(jd.__dict__) if jd else "No job description provided."

        prompt = QUESTION_GENERATION_PROMPT.format(
            num_questions=num_questions,
            interview_type=interview_type,
            interview_subtype=interview_subtype,
            difficulty=difficulty,
            target_role=target_role,
            resume_context=resume_context,
            jd_context=jd_context,
        )

        try:
            response_text = await self.llm.generate(
                prompt=prompt,
                system_prompt="You are an expert interviewer. Provide questions as a JSON block only.",
                temperature=0.7,
            )

            clean_text = response_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            data = json.loads(clean_text)
            questions = []
            for item in data.get("questions", []):
                questions.append(
                    GeneratedQuestion(
                        question_text=item.get("question_text", ""),
                        question_type=item.get("question_type", "general"),
                        difficulty=item.get("difficulty", "medium"),
                        expected_answer=item.get("expected_answer", ""),
                        evaluation_rubric=item.get("evaluation_rubric", {}),
                        tags=item.get("tags", []),
                    )
                )
            return questions
        except Exception as e:
            logger.error(f"Error generating questions via LLM: {e}")
            # Mock fallback question
            return [
                GeneratedQuestion(
                    question_text="Tell me about yourself and your experience with FastAPI and LangGraph.",
                    question_type="behavioral",
                    difficulty=difficulty,
                    expected_answer="A standard STAR method response highlighting core achievements.",
                    evaluation_rubric={},
                )
            ]
