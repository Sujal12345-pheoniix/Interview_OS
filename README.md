# ⭐ InterviewOS

> **The AI-Powered Interview Operating System** — Increase your interview success rate by 3x.

[![License: MIT](https://img.shields.io/badge/License-MIT-violet.svg)](https://opensource.org/licenses/MIT)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-3178C6?logo=typescript)](https://typescriptlang.org)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://python.org)

---

## 🚀 What is InterviewOS?

InterviewOS is a production-grade, AI-powered Interview Operating System that goes far beyond simple mock interviews. It's a complete platform that:

- 🎙️ **Conducts realistic AI voice interviews** — feels like a real human interviewer
- 🧠 **Diagnoses your weaknesses** using 9 specialized AI agents
- 📋 **Analyzes your resume and job descriptions** to generate personalized questions  
- 📈 **Builds 90-day learning plans** tailored to your gaps
- 📊 **Tracks your progress** with skill graphs and trend analysis
- 🏆 **Generates detailed post-interview reports** with hiring recommendations

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎙️ Voice AI Interviewer | Real-time voice with interruptions, follow-ups, cross-questioning |
| 📄 Resume + JD Analysis | Extract skills, detect gaps, match score |
| 🤖 9 Specialized AI Agents | Resume Analyzer, Question Generator, Communication Evaluator, etc. |
| 📊 Post-Interview Report | 12-dimension scoring + 90-day improvement plan |
| 🎯 All Interview Types | SE, Non-Tech, Government Exams, Higher Education |
| 📈 Progress Dashboard | Skill graph, weakness trends, readiness score |
| 🌙 Premium Dark UI | Linear/Stripe-inspired glassmorphism design |

---

## 🎯 Interview Types

### Software Engineering
- DSA & Algorithms
- Backend Engineering
- Frontend Engineering
- Full Stack
- Platform & DevOps
- AI/ML & Data Science
- Cybersecurity

### Non-Technical
- HR & Behavioral
- Sales & Marketing
- Product Management
- Customer Support

### Government Exams
- UPSC, SSC, Banking, Railway, State PCS

### Higher Education
- MBA Interviews
- University Admissions
- Scholarships

---

## 🏗️ Architecture

```
interviewos/
├── frontend/           # Next.js 15 + TypeScript + Tailwind + ShadCN
├── backend/            # FastAPI + LangGraph Multi-Agent System
├── docs/               # Architecture, API Design, PRD, Roadmap
├── docker-compose.yml  # Local development
└── .github/            # CI/CD workflows
```

### Tech Stack

**Frontend**: Next.js 15, TypeScript, Tailwind CSS, ShadCN UI, Framer Motion, TanStack Query, Zustand  
**Backend**: FastAPI, Python 3.11, LangGraph, SQLAlchemy, Alembic  
**Database**: PostgreSQL + pgvector, Redis, Qdrant (vector DB)  
**AI**: Gemini 2.5 Flash (primary), OpenRouter (fallback), BGE-Small embeddings  
**Voice**: Deepgram (STT), Cartesia (TTS)  
**Auth**: Clerk  
**Storage**: Cloudflare R2  
**Queue**: BullMQ / Celery  
**Deploy**: Vercel (frontend), Fly.io/Railway (backend)  
**Monitor**: Sentry, PostHog  

---

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL 16+
- Redis 7+

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/interviewos.git
cd interviewos
```

### 2. Start infrastructure with Docker
```bash
docker-compose up -d postgres redis qdrant
```

### 3. Setup Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
cp .env.example .env            # Fill in your API keys
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

### 4. Setup Frontend
```bash
cd frontend
npm install
cp .env.local.example .env.local  # Fill in your keys
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) 🎉

---

## 📋 Documentation

| Document | Description |
|----------|-------------|
| [📋 PRD](./docs/PRD.md) | Full Product Requirements Document |
| [🏗️ System Architecture](./docs/SYSTEM_ARCHITECTURE.md) | Technical architecture & folder structure |
| [🗄️ Database Schema](./docs/DATABASE_SCHEMA.md) | Full PostgreSQL schema + ERD |
| [🔌 API Design](./docs/API_DESIGN.md) | REST + WebSocket API specification |
| [🤖 Agent Architecture](./docs/AGENT_ARCHITECTURE.md) | Multi-agent system design |
| [💬 Prompt Library](./docs/PROMPT_LIBRARY.md) | Production prompts for all 9 agents |
| [🎨 UI Design System](./docs/UI_DESIGN_SYSTEM.md) | Colors, typography, components |
| [🗺️ Roadmap](./docs/ROADMAP.md) | MVP & Enterprise roadmap |
| [🚀 Deployment Guide](./docs/DEPLOYMENT_GUIDE.md) | Deploy to Vercel, Fly.io, Railway, Supabase |
| [💰 Cost Analysis](./docs/COST_ANALYSIS.md) | Per-interview cost & pricing model |
| [🔒 Security](./docs/SECURITY.md) | Security architecture & compliance |
| [✅ Production Checklist](./docs/PRODUCTION_CHECKLIST.md) | 100+ item launch checklist |
| [🖱️ Cursor Instructions](./docs/CURSOR_INSTRUCTIONS.md) | AI-assisted development guide |

---

## 🌐 Free Deployment Options

### Frontend: Vercel (Free Tier)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

### Backend: Multiple Free Options
- **Fly.io** — 3 free VMs (best for FastAPI + WebSockets)
- **Render** — Free tier with spin-down
- **Hugging Face Spaces** — Free Docker deployment
- **Zeabur** — Developer credits
- **Koyeb** — Free nano instance

### Database & Services (Free Tiers)
- **Supabase** — Free PostgreSQL + vector search + auth
- **Upstash** — Free Redis
- **Qdrant Cloud** — Free 1GB cluster
- **Clerk** — Free up to 10k MAU

---

## 🤖 The 9 AI Agents

```
Agent 1: Resume Analyzer      → Extracts skills, projects, detects gaps
Agent 2: JD Analyzer          → Parses requirements, culture signals
Agent 3: Question Generator   → Creates adaptive, role-specific questions
Agent 4: Interview Conductor  → Manages flow, follow-ups, cross-questions
Agent 5: Communication Eval   → Scores clarity, STAR method, structure
Agent 6: Technical Evaluator  → Grades technical depth & problem-solving
Agent 7: Behavioral Evaluator → Assesses leadership, teamwork, culture fit
Agent 8: Learning Coach       → Builds 90-day personalized learning plan
Agent 9: Progress Tracker     → Tracks trends, skill velocity, readiness
```

---

## 📊 Post-Interview Report

Every interview generates a comprehensive report:

- **Overall Score** (0-100)
- **Communication Score** — clarity, structure, STAR method
- **Technical Score** — depth, accuracy, problem-solving
- **Problem Solving Score** — approach, optimization
- **Confidence Score** — delivery, pacing, filler words
- **Leadership Score** — initiative, ownership, impact
- **Hiring Recommendation** — Strong Hire / Hire / No Hire
- **Strengths & Weaknesses**
- **Missed Opportunities**
- **Better Answer Examples**
- **90-Day Improvement Plan**

---

## 💰 Pricing

| Plan | Price | Features |
|------|-------|---------|
| Free | $0 | 3 interviews/month, text only |
| Pro | $19/mo | Unlimited, voice, all reports |
| Enterprise | Custom | Team, SSO, API, custom branding |

---

## 🔐 Environment Variables

See [backend/.env.example](./backend/.env.example) and [frontend/.env.local.example](./frontend/.env.local.example) for all required variables.

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/ -v --cov=app

# Frontend tests
cd frontend
npm test

# E2E tests
npm run test:e2e
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 🙏 Built By

**InterviewOS Team** — A team of engineers from Google, OpenAI, Amazon, and YC-backed founders building the future of career development.

---

<p align="center">Made with ❤️ to help people land their dream jobs</p>
