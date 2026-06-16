from __future__ import annotations

from loguru import logger
from app.services.llm_service import LLMService
from app.prompts.interview_prompts import INTERVIEW_CONDUCTOR_SYSTEM_PROMPT


class InterviewConductorAgent:
    """Agent 4: Conducts the active dialogue, handles follow-up probing, and detects avoidance."""

    def __init__(self):
        self.llm = LLMService()

    async def generate_response(
        self,
        current_question: str,
        user_response: str,
        chat_history: list[dict],
    ) -> str:
        logger.info("Generating next follow-up/response in interview flow...")

        history_context = ""
        for msg in chat_history:
            role = msg.get("role", "user")
            text = msg.get("content", "")
            history_context += f"{role.upper()}: {text}\n"

        prompt = f"""Conversation history:
{history_context}
Current Question being answered: {current_question}
Candidate's response: {user_response}

Please generate the next interviewer response. You should acknowledge their answer briefly, probe/follow-up if needed, or transition to the next stage if satisfied. Ensure it is conversational and short (max 2-3 sentences)."""

        try:
            response_text = await self.llm.generate(
                prompt=prompt,
                system_prompt=INTERVIEW_CONDUCTOR_SYSTEM_PROMPT,
                temperature=0.7,
            )
            return response_text.strip()
        except Exception as e:
            logger.error(f"Error conducting dialogue flow: {e}")
            return "Thank you for sharing that. Let's move on to the next question."
