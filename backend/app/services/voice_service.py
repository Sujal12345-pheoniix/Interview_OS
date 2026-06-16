from __future__ import annotations

import httpx
from loguru import logger
from app.core.config import settings

class VoiceService:
    """STT (Deepgram) and TTS (Cartesia) Client wrapper."""

    def __init__(self):
        self.deepgram_api_key = settings.DEEPGRAM_API_KEY
        self.cartesia_api_key = settings.CARTESIA_API_KEY

    async def transcribe_audio(self, audio_bytes: bytes) -> str:
        """Call Deepgram API to transcribe raw audio bytes."""
        if not self.deepgram_api_key:
            logger.warning("Deepgram API key not configured. Returning mock transcription.")
            return "FastAPI is a modern web framework."

        headers = {
            "Authorization": f"Token {self.deepgram_api_key}",
            "Content-Type": "audio/wav",
        }
        url = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, content=audio_bytes, timeout=10.0)
                if response.status_code == 200:
                    data = response.json()
                    transcript = data.get("results", {}).get("channels", [{}])[0].get("alternatives", [{}])[0].get("transcript", "")
                    return transcript
                else:
                    logger.error(f"Deepgram error: {response.text}")
            except Exception as e:
                logger.error(f"Failed to transcribe audio via Deepgram: {e}")

        return ""

    async def synthesize_speech(self, text: str) -> bytes:
        """Call Cartesia API to synthesize text to speech audio bytes (mp3/wav)."""
        if not self.cartesia_api_key:
            logger.warning("Cartesia API key not configured. Returning empty audio bytes.")
            return b""

        headers = {
            "Cartesia-Version": "2024-06-18",
            "X-API-Key": self.cartesia_api_key,
            "Content-Type": "application/json",
        }
        url = "https://api.cartesia.ai/tts/bytes"
        payload = {
            "model_id": "sonic-english",
            "transcript": text,
            "voice": {
                "mode": "id",
                "id": "a0e998ae-05cd-4abc-8af7-ae040010087c",  # Standard male voice
            },
            "output_format": {
                "container": "raw",
                "encoding": "pcm_s16le",
                "sample_rate": 16000,
            },
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=payload, timeout=15.0)
                if response.status_code == 200:
                    return response.content
                else:
                    logger.error(f"Cartesia error: {response.text}")
            except Exception as e:
                logger.error(f"Failed to synthesize speech via Cartesia: {e}")

        return b""
