import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from loguru import logger
from app.services.voice_service import VoiceService

router = APIRouter()
voice_service = VoiceService()

@router.websocket("/interview/{interview_id}")
async def voice_interview_websocket(websocket: WebSocket, interview_id: str):
    """
    Main WebSocket connection for real-time voice streaming mock interviews.
    """
    await websocket.accept()
    logger.info(f"WebSocket voice connection accepted for interview {interview_id}")

    try:
        # Send initial intro question
        intro_text = "Hello! Welcome to your mock interview. Let's start with: Tell me about yourself."
        audio_bytes = await voice_service.synthesize_speech(intro_text)
        
        await websocket.send_json({
            "type": "question",
            "text": intro_text,
            "index": 1,
            "total": 5
        })
        
        if audio_bytes:
            import base64
            await websocket.send_json({
                "type": "audio_response",
                "data": base64.b64encode(audio_bytes).decode("utf-8")
            })

        while True:
            # Main socket event loop
            data = await websocket.receive_text()
            message = json.loads(data)
            logger.info(f"Received WebSocket frame: {message.get('type')}")

            if message.get("type") == "end_interview":
                await websocket.send_json({"type": "interview_complete", "session_id": interview_id})
                break

    except WebSocketDisconnect:
        logger.info(f"WebSocket voice disconnected for interview {interview_id}")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
