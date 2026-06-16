from __future__ import annotations

import asyncio
import json
import time
from typing import Any, AsyncGenerator, Optional

import google.generativeai as genai
from loguru import logger
from openai import AsyncOpenAI

from app.core.config import settings

# ─── Configure Gemini ─────────────────────────────────────────────────────────
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

# ─── Gemini Model Config ──────────────────────────────────────────────────────
_GENERATION_CONFIG = {
    "temperature": settings.GEMINI_TEMPERATURE,
    "max_output_tokens": settings.GEMINI_MAX_TOKENS,
    "response_mime_type": "text/plain",
}

_JSON_GENERATION_CONFIG = {
    "temperature": 0.3,
    "max_output_tokens": settings.GEMINI_MAX_TOKENS,
    "response_mime_type": "application/json",
}


class LLMService:
    """
    LLM Service with Gemini 2.5 Flash as primary and OpenRouter as fallback.
    Supports: text generation, JSON generation, streaming.
    """

    def __init__(self):
        self._gemini_model = genai.GenerativeModel(settings.GEMINI_MODEL)
        self._openrouter_client: Optional[AsyncOpenAI] = None
        if settings.OPENROUTER_API_KEY:
            self._openrouter_client = AsyncOpenAI(
                api_key=settings.OPENROUTER_API_KEY,
                base_url=settings.OPENROUTER_BASE_URL,
            )

    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        use_fallback: bool = True,
    ) -> str:
        """Generate text using Gemini 2.5 Flash with fallback to OpenRouter"""
        for attempt in range(settings.LLM_MAX_RETRIES):
            try:
                result = await self._gemini_generate(
                    prompt=prompt,
                    system_prompt=system_prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                return result
            except Exception as e:
                logger.warning(f"Gemini attempt {attempt + 1} failed: {e}")
                if attempt < settings.LLM_MAX_RETRIES - 1:
                    await asyncio.sleep(settings.LLM_RETRY_DELAY * (2 ** attempt))
                elif use_fallback and self._openrouter_client:
                    logger.info("Falling back to OpenRouter")
                    return await self._openrouter_generate(
                        prompt=prompt,
                        system_prompt=system_prompt,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    )
                else:
                    raise

        raise RuntimeError("All LLM attempts failed")

    async def generate_json(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.3,
    ) -> dict[str, Any]:
        """Generate structured JSON output"""
        try:
            model = genai.GenerativeModel(
                model_name=settings.GEMINI_MODEL,
                generation_config=_JSON_GENERATION_CONFIG,
                system_instruction=system_prompt or "Return valid JSON only.",
            )
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: model.generate_content(prompt)
            )
            text = response.text.strip()
            # Clean JSON fences if present
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from LLM: {e}")
            raise ValueError(f"LLM returned invalid JSON: {e}")
        except Exception as e:
            logger.error(f"JSON generation failed: {e}")
            raise

    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:
        """Stream text generation token by token"""
        try:
            model = genai.GenerativeModel(
                model_name=settings.GEMINI_MODEL,
                system_instruction=system_prompt,
            )
            # Run in executor since Gemini SDK isn't fully async
            loop = asyncio.get_event_loop()

            def _stream():
                return model.generate_content(prompt, stream=True)

            stream = await loop.run_in_executor(None, _stream)
            for chunk in stream:
                if chunk.text:
                    yield chunk.text
                    await asyncio.sleep(0)  # Allow event loop to breathe
        except Exception as e:
            logger.error(f"Streaming failed: {e}")
            raise

    async def _gemini_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """Internal Gemini generation"""
        config = _GENERATION_CONFIG.copy()
        if temperature is not None:
            config["temperature"] = temperature
        if max_tokens is not None:
            config["max_output_tokens"] = max_tokens

        model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL,
            generation_config=config,
            system_instruction=system_prompt,
        )

        loop = asyncio.get_event_loop()
        start = time.monotonic()
        response = await loop.run_in_executor(
            None,
            lambda: model.generate_content(prompt)
        )
        elapsed = time.monotonic() - start
        logger.debug(f"Gemini response in {elapsed:.2f}s — {len(response.text)} chars")
        return response.text

    async def _openrouter_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """Internal OpenRouter generation"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = await self._openrouter_client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=messages,
            temperature=temperature or settings.GEMINI_TEMPERATURE,
            max_tokens=max_tokens or settings.GEMINI_MAX_TOKENS,
        )
        return response.choices[0].message.content or ""

    async def count_tokens(self, text: str) -> int:
        """Count tokens for cost estimation"""
        model = genai.GenerativeModel(settings.GEMINI_MODEL)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, lambda: model.count_tokens(text))
        return result.total_tokens


# Global LLM service instance
llm_service = LLMService()
