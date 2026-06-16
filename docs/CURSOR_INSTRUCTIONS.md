# InterviewOS — Cursor Implementation Plan

> This document tells Cursor AI exactly how to implement each feature. Follow this in order for fastest development velocity.

---

## Setup Instructions for Cursor

### 1. Open Both Projects
- Open `d:/Desktop/PROJECTS/interview-simulator` in Cursor
- Use split terminal: one for `backend/`, one for `frontend/`

### 2. Install Cursor Rules
Create `.cursorrules` in the root with:
```
You are an expert full-stack engineer building InterviewOS.
- Backend: FastAPI + Python 3.11, SQLAlchemy 2.0, LangGraph, async throughout
- Frontend: Next.js 15 App Router, TypeScript strict mode, Tailwind, Framer Motion
- Always use async/await, never synchronous database calls
- Always add proper TypeScript types, never use `any`
- Follow the design system in docs/UI_DESIGN_SYSTEM.md for all UI work
- Use the prompts in docs/PROMPT_LIBRARY.md for all LLM integrations
- All API routes go in app/api/v1/
- All agents go in app/agents/
```

---

## Phase 1: Environment Setup (Day 1)

### 1.1 Backend Environment
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Fill in: GEMINI_API_KEY, DATABASE_URL, REDIS_URL
alembic upgrade head
uvicorn app.main:app --reload
```

### 1.2 Frontend Environment
```bash
cd frontend
npm install
cp .env.local.example .env.local
# Fill in: NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY, CLERK_SECRET_KEY, NEXT_PUBLIC_API_URL
npm run dev
```

### 1.3 Infrastructure (Docker)
```bash
docker-compose up -d postgres redis qdrant
```

**Verify setup:**
- Backend health: `GET http://localhost:8000/health`
- Frontend: `http://localhost:3000`
- Qdrant dashboard: `http://localhost:6333/dashboard`

---

## Phase 2: Database & Models (Day 1-2)

### Cursor Prompt for Models:
```
Implement the SQLAlchemy models in backend/app/models/ based on the schema in docs/DATABASE_SCHEMA.md.
Use SQLAlchemy 2.0 async syntax with `Mapped` and `mapped_column`.
Add all relationships, indexes, and constraints as specified.
```

### Run migrations:
```bash
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

---

## Phase 3: Core API Endpoints (Day 2-3)

### Implementation Order:
1. `app/api/v1/auth.py` — Clerk webhook sync
2. `app/api/v1/users.py` — Profile CRUD
3. `app/api/v1/resumes.py` — Upload + parsing trigger
4. `app/api/v1/interviews.py` — Interview CRUD + start/end
5. `app/api/v1/voice.py` — WebSocket handler

### Cursor Prompt for Auth:
```
Implement the Clerk webhook handler in backend/app/api/v1/auth.py.
The webhook should:
1. Verify Clerk webhook signature using svix
2. On user.created event: create User record in PostgreSQL
3. On user.updated event: update User record
4. On user.deleted event: soft-delete User record
Use the User model from app/models/user.py.
```

### Cursor Prompt for Interviews:
```
Implement the interview CRUD endpoints in backend/app/api/v1/interviews.py.
Follow the API spec in docs/API_DESIGN.md.
POST /interviews/start should:
1. Create Interview record
2. Trigger the LangGraph agent orchestration via background task
3. Return interview_id and websocket_url
Use proper async SQLAlchemy queries with get_db dependency.
```

---

## Phase 4: Multi-Agent System (Day 3-5)

### Implementation Order:
1. `app/agents/state.py` — InterviewState TypedDict
2. `app/agents/resume_analyzer.py` — Agent 1
3. `app/agents/jd_analyzer.py` — Agent 2
4. `app/agents/question_generator.py` — Agent 3
5. `app/agents/orchestrator.py` — LangGraph graph
6. `app/agents/interview_conductor.py` — Agent 4
7. Evaluator agents (5, 6, 7) — After interview
8. `app/agents/learning_coach.py` — Agent 8
9. `app/agents/progress_tracker.py` — Agent 9

### Cursor Prompt for Resume Analyzer:
```
Implement Agent 1 (Resume Analyzer) in backend/app/agents/resume_analyzer.py.
Use the prompts from backend/app/prompts/resume_prompts.py.
The agent should:
1. Accept raw resume text as input
2. Call Gemini 2.5 Flash with the RESUME_EXTRACTION_PROMPT
3. Parse the JSON output into ResumeAnalysis dataclass
4. Generate embeddings using sentence-transformers BGE-small
5. Store embeddings in Qdrant with metadata
6. Return skills list, projects list, gaps list
Handle errors gracefully with fallback to basic regex extraction.
```

### Cursor Prompt for LangGraph Orchestrator:
```
Implement the LangGraph StateGraph orchestrator in backend/app/agents/orchestrator.py.
Wire all 9 agents as nodes.
Use conditional edges:
- If resume uploaded → run resume_analyzer first
- If jd uploaded → run jd_analyzer (parallel with resume_analyzer)
- Always run question_generator after analyzers
- Run interview_conductor as the main interview loop
- After interview ends → run evaluators in parallel (communication, technical, behavioral)
- Run learning_coach after evaluation
- Run progress_tracker last
Compile the graph and expose build_interview_graph() function.
```

---

## Phase 5: Voice Interview (Day 4-6)

### Cursor Prompt for Voice WebSocket:
```
Implement the WebSocket endpoint for voice interviews in backend/app/api/v1/voice.py.
The WebSocket should:
1. Accept connection at ws://localhost:8000/v1/voice/interview/{interview_id}
2. Authenticate using Clerk token in query param
3. Stream audio bytes from client to Deepgram STT
4. When Deepgram returns transcript, send to Interview Conductor agent
5. Get AI response text from agent
6. Stream TTS audio back to client using Cartesia
7. Maintain interview state in Redis
8. Handle disconnections and reconnections
9. Save full transcript to database on end

Message protocol:
- Client → Server: { type: "audio_chunk", data: base64_audio }
- Client → Server: { type: "end_interview" }
- Server → Client: { type: "transcript", text: "...", speaker: "user"|"ai" }
- Server → Client: { type: "audio_response", data: base64_audio }
- Server → Client: { type: "question", text: "...", index: 1, total: 10 }
- Server → Client: { type: "interview_complete", session_id: "..." }
```

---

## Phase 6: Frontend Pages (Day 5-8)

### Implementation Order:
1. Landing page (`app/page.tsx`)
2. Auth pages (Clerk)
3. Dashboard layout + sidebar
4. New interview wizard
5. Voice interview interface
6. Post-interview report
7. Progress dashboard
8. Resume manager

### Cursor Prompt for Landing Page:
```
Implement the landing page in frontend/src/app/page.tsx.
Use Framer Motion for all animations.
Follow the design system in docs/UI_DESIGN_SYSTEM.md.
The page should include:
1. Animated navigation bar with glassmorphism
2. Hero section with gradient text "Land Your Dream Job" and floating orbs
3. Statistics counter (animate numbers from 0 to target on scroll)
4. Feature grid (6 glassmorphism cards with hover animations)
5. Testimonials section
6. Pricing section (3 tiers)
7. CTA section
8. Footer
Make it look better than Linear.app in terms of aesthetics.
```

### Cursor Prompt for Voice Interface:
```
Implement the voice interview UI in frontend/src/app/(dashboard)/interview/[id]/page.tsx.
Components to use:
- AudioVisualizer (src/components/ui/audio-visualizer.tsx)
- AgentStatusFeed (src/components/interview/agent-status-feed.tsx)
- VoiceInterface (src/components/interview/voice-interface.tsx)
Connect to WebSocket at NEXT_PUBLIC_WS_URL/v1/voice/interview/{id}
Handle: audio recording with MediaRecorder API, streaming audio playback, transcript display.
Show AI speaking animation (pulsing rings) when receiving audio.
```

---

## Phase 7: Report Generation (Day 7-9)

### Cursor Prompt for Report:
```
Implement the post-interview report page in frontend/src/app/(dashboard)/interview/[id]/report/page.tsx.
Fetch data from GET /api/v1/interviews/{id}/report.
Display:
1. Overall score with animated ProgressRing component
2. Score breakdown cards (use score-breakdown.tsx)
3. Hiring recommendation badge (color-coded)
4. Strengths (green checkmarks)
5. Weaknesses (red X marks)  
6. Better answer examples (expandable accordion)
7. 90-day learning plan (use learning-plan-timeline.tsx)
All elements should animate in with staggered entrance using Framer Motion.
```

---

## Phase 8: Analytics & Progress (Day 8-10)

### Cursor Prompt for Progress Dashboard:
```
Implement the progress dashboard in frontend/src/app/(dashboard)/progress/page.tsx.
Use recharts for all charts.
Charts to implement:
1. LineChart: interview scores over time (last 30 days)
2. RadarChart: skill profile (6 dimensions)
3. BarChart: score comparison by interview type
4. Custom heatmap: interview frequency calendar
Fetch from GET /api/v1/analytics/progress.
```

---

## Phase 9: Testing (Day 9-11)

### Backend Tests:
```bash
# Cursor prompt: Write pytest tests for all API endpoints
# Test file: backend/tests/test_interviews.py
pytest tests/ -v --cov=app
```

### Frontend Tests:
```bash
# Cursor prompt: Write React Testing Library tests for key components
npm test
```

### Load Testing:
```bash
# Install k6
k6 run scripts/load-test.js
```

---

## Phase 10: Deployment (Day 11-14)

### Deploy to Fly.io (Backend):
```bash
cd backend
fly launch --name interviewos-api
fly secrets set GEMINI_API_KEY=... DATABASE_URL=...
fly deploy
```

### Deploy to Vercel (Frontend):
```bash
cd frontend
vercel --prod
# Set all environment variables in Vercel dashboard
```

### GitHub Push:
```bash
git add .
git commit -m "feat: InterviewOS initial production release"
git remote add origin https://github.com/YOUR_USERNAME/interviewos.git
git push -u origin main
```

---

## Cursor Tips & Shortcuts

### Effective Cursor Prompts
1. Always reference specific files: "In `backend/app/agents/resume_analyzer.py`..."
2. Mention the docs: "Follow the schema in `docs/DATABASE_SCHEMA.md`..."
3. Ask for complete files: "Write the complete implementation, no TODOs"
4. Iterate: "The previous implementation missing error handling, add try/catch..."

### Key Cursor Commands
- `Cmd+K` — Inline edit with prompt
- `Cmd+L` — Open chat with selected code
- `Cmd+Shift+P` — Command palette
- `@file` — Reference a specific file in chat

### Recommended AI Chat Patterns
```
# Pattern 1: Feature Implementation
"Implement [feature] in [file]. It should:
1. [requirement 1]
2. [requirement 2]
Follow the spec in [docs/FILE.md]."

# Pattern 2: Bug Fix
"The [function] in [file] is failing with [error].
Here's the code: [paste code]
Fix it and explain why."

# Pattern 3: Integration
"Connect [component A] to [component B].
A outputs: [data shape]
B expects: [data shape]
Write the integration code."
```

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `CORS error` | Add frontend URL to ALLOWED_ORIGINS in backend .env |
| `WebSocket disconnect` | Increase Fly.io timeout to 300s in fly.toml |
| `Qdrant connection` | Ensure QDRANT_URL matches docker-compose service name |
| `Clerk 401` | Verify CLERK_SECRET_KEY is set correctly |
| `Gemini rate limit` | Implement exponential backoff in llm_service.py |
| `Audio not playing` | Check Cartesia API key and audio format (PCM 16-bit) |
| `Alembic conflict` | Run `alembic heads` then merge heads |

---

## Environment Variables Quick Reference

### Must Have for MVP
```
GEMINI_API_KEY         — Gemini 2.5 Flash (primary LLM)
DATABASE_URL           — PostgreSQL connection string
REDIS_URL              — Redis connection string
CLERK_SECRET_KEY       — Backend Clerk auth
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY — Frontend Clerk auth
DEEPGRAM_API_KEY       — Voice STT
CARTESIA_API_KEY       — Voice TTS
NEXT_PUBLIC_API_URL    — Backend URL from frontend
```

### Nice to Have
```
QDRANT_API_KEY         — If using Qdrant Cloud (not local)
CLOUDFLARE_R2_*        — File uploads
SENTRY_DSN             — Error monitoring
POSTHOG_API_KEY        — Analytics
OPENROUTER_API_KEY     — LLM fallback
```
