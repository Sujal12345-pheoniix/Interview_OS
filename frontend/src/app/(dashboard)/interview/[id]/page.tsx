"use client";

import React, { useState, useEffect, useRef } from "react";
import { useRouter, useParams } from "next/navigation";
import { Mic, MicOff, Video, VideoOff, PhoneOff, AlertCircle, Loader2 } from "lucide-react";

export default function VoiceInterview() {
  const router = useRouter();
  const params = useParams();
  const interviewId = params?.id || "mock-session-id";

  const [wsConnected, setWsConnected] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [currentQuestion, setCurrentQuestion] = useState("Connecting to voice systems...");
  const [transcript, setTranscript] = useState<string[]>([]);
  const [speaking, setSpeaking] = useState(false);

  const socketRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    // Connect to mockup WS route matching mock API voice layout
    const wsUrl = `ws://localhost:8000/v1/voice/interview/${interviewId}`;
    const socket = new WebSocket(wsUrl);

    socket.onopen = () => {
      setWsConnected(true);
      setCurrentQuestion("Tell me about yourself.");
    };

    socket.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        if (message.type === "question") {
          setCurrentQuestion(message.text);
          setTranscript((prev) => [...prev, `Interviewer: ${message.text}`]);
          setSpeaking(true);
          // Turn off speaking state after 3 seconds
          setTimeout(() => setSpeaking(false), 3000);
        }
      } catch (err) {
        console.error("Failed to parse WS package", err);
      }
    };

    socketRef.current = socket;

    return () => {
      socket.close();
    };
  }, [interviewId]);

  const handleEnd = () => {
    if (socketRef.current) {
      socketRef.current.send(JSON.stringify({ type: "end_interview" }));
    }
    router.push(`/interview/${interviewId}/report`);
  };

  return (
    <div className="max-w-4xl mx-auto flex flex-col items-center gap-10">
      {/* Speaking Indicator Panel */}
      <div className="relative w-full aspect-video md:aspect-[21/9] glass-card flex flex-col items-center justify-center gap-6 overflow-hidden">
        {/* Animated speaking pulses */}
        {speaking && (
          <>
            <div className="absolute w-40 h-40 rounded-full border-2 border-cyan-500/20 animate-ping" />
            <div className="absolute w-56 h-56 rounded-full border-2 border-cyan-500/10 animate-ping [animation-delay:0.3s]" />
          </>
        )}

        <div className="w-24 h-24 rounded-full bg-cyan-950/40 border border-cyan-500/30 flex items-center justify-center relative z-10">
          <Loader2 className={`w-12 h-12 text-cyan-400 ${speaking ? "animate-spin" : "animate-pulse"}`} />
        </div>

        <div className="text-center relative z-10 max-w-xl px-6">
          <div className="text-xs uppercase tracking-widest text-cyan-500 font-bold mb-2">AI Interviewer Speaking</div>
          <h2 className="text-xl md:text-2xl font-extrabold tracking-tight">{currentQuestion}</h2>
        </div>
      </div>

      {/* Transcript Log */}
      <div className="w-full glass-card p-6 min-h-[150px] max-h-[250px] overflow-y-auto flex flex-col gap-3">
        <div className="text-xs text-zinc-500 font-bold uppercase tracking-wider">Conversation Log</div>
        <div className="flex flex-col gap-2">
          {transcript.length === 0 ? (
            <div className="text-sm text-zinc-600">Waiting for live conversation transcript...</div>
          ) : (
            transcript.map((line, idx) => (
              <div key={idx} className="text-sm text-zinc-300 font-medium">
                {line}
              </div>
            ))
          )}
        </div>
      </div>

      {/* Session Controls */}
      <div className="flex gap-6 items-center">
        <button
          onClick={() => setIsMuted(!isMuted)}
          className={`w-14 h-14 rounded-full flex items-center justify-center border transition-all ${
            isMuted
              ? "bg-red-500/20 border-red-500 text-red-500 hover:bg-red-500/30"
              : "bg-zinc-900/50 border-zinc-800 text-zinc-400 hover:text-white hover:bg-zinc-800"
          }`}
        >
          {isMuted ? <MicOff className="w-6 h-6" /> : <Mic className="w-6 h-6" />}
        </button>

        <button
          onClick={handleEnd}
          className="px-8 py-4 rounded-full font-bold bg-red-600 hover:bg-red-500 text-white flex items-center gap-2 shadow-lg shadow-red-500/20 transition-all"
        >
          <PhoneOff className="w-5 h-5" /> End Mock Session
        </button>
      </div>
    </div>
  );
}
