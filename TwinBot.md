# TwinBot

A personal AI agent platform that serves as your digital twin — featuring multi-agent orchestration, RAG (Retrieval-Augmented Generation), MCP tool integration, voice I/O, and autonomous task execution.

## Features

- **Multi-Agent Architecture** — Seven agent types (Reactive, Proactive, BDI, Learning, Autonomous, Collaborative, Hybrid) with intelligent routing
- **Chat Interface** — REST API + WebSocket streaming with real-time responses
- **RAG Pipeline** — Document upload, ingestion, and semantic search powered by ChromaDB
- **Memory System** — Short-term, episodic, and long-term memory with fact extraction and knowledge linking
- **Voice I/O** — Speech-to-text (Whisper) and text-to-speech (OpenAI TTS / Piper) with real-time mic streaming
- **MCP Tools** — Filesystem, web search, GitHub, browser automation, document generation, calculator, and more
- **Scheduler** — Cron-based and interval-based task scheduling with triggers
- **Skills Registry** — Extensible plugin system for custom capabilities
- **Guardrails** — Safety engine with configurable budget limits
- **Metrics & Analytics** — Real-time activity streams, execution traces, and performance dashboards
- **RBAC** — Row-level security via Supabase (optional)
- **Sentry Integration** — Error monitoring (optional)

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | FastAPI, Python 3.11+, Uvicorn |
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS, Zustand |
| **LLM** | Anthropic (Claude Sonnet 4), OpenAI (fallback), Ollama (local) |
| **Vector DB** | ChromaDB with sentence-transformers (all-MiniLM-L6-v2) |
| **Database** | SQLite (local) / Supabase PostgreSQL (cloud) |
| **Voice** | OpenAI Whisper / faster-whisper (STT), OpenAI TTS / piper-tts (TTS) |
| **Deployment** | Docker, Railway (backend), Vercel (frontend) |

## Architecture

```
User (Browser)
      ↓
Frontend (React/Vite) :9200
      ↓
API Gateway (FastAPI) :9100
      ↓
AgentBridge (orchestration)
      ↓
Agent Types ─── Reactive │ Proactive │ BDI │ Learning │ Autonomous │ Collaborative │ Hybrid
      ↓
Services
  ├─ LLMService (Anthropic / OpenAI / Ollama)
  ├─ RAGService (ChromaDB + embeddings)
  ├─ MemoryPipeline (facts → knowledge graph)
  ├─ VoiceEngine (Whisper / Piper)
  ├─ JobService (background tasks)
  ├─ SchedulerService (cron / interval)
  └─ Tools & Skills (MCP servers, plugins)
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+
- An Anthropic API key (or OpenAI key as fallback)

### Environment Variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your-key-here

# Optional
OPENAI_API_KEY=your-key
GITHUB_TOKEN=your-token
SUPABASE_URL=your-url
SUPABASE_KEY=your-key
SENTRY_DSN=your-dsn
```

### One-Click Launch (Windows)

```bash
python launcher.py
```

This starts both backend and frontend, waits for health checks, and opens the browser.

Options:
```bash
python launcher.py --no-browser      # Skip auto-opening browser
python launcher.py --backend-only    # Backend only
```

Or use the included batch script:
```bash
start-twinbot.bat
```

### Manual Setup

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 9100
```

**Frontend (separate terminal):**
```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker-compose up --build
```

The app will be available at `[URL_REMOVED]

## API Endpoints

### Chat
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat/send` | Send a message |
| WS | `/api/chat/stream` | WebSocket streaming |

### Agents
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/agents` | List all agent states |
| GET | `/api/agents/status` | Orchestrator status |
| PUT | `/api/agents/mode` | Switch agent mode |
| GET | `/api/agents/modes/list` | Available modes |

### RAG (Documents)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/rag/upload` | Upload a document |
| POST | `/api/rag/ingest/{doc_id}` | Process a document |
| GET | `/api/rag/documents` | List documents |
| POST | `/api/rag/query` | Semantic search |
| GET | `/api/rag/stats` | RAG statistics |

### Memory
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/memory/stats` | Memory statistics |
| POST | `/api/memory/add` | Store a memory |
| POST | `/api/memory/recall` | Query memories |
| DELETE | `/api/memory/{scope}` | Clear memories |

### Voice
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/voice/transcribe` | Audio → text |
| POST | `/api/voice/speak` | Text → audio |
| GET | `/api/voice/voices` | List TTS voices |
| WS | `/api/voice/ws` | Real-time mic streaming |

### Tools & Skills
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tools` | List available tools |
| POST | `/api/tools/test` | Test a tool |
| GET | `/api/skills` | List all skills |
| POST | `/api/skills/invoke` | Execute a skill |

### Other
| Endpoint | Description |
|----------|-------------|
| `/api/scheduler/schedules` | Schedule management |
| `/api/metrics/dashboard` | Dashboard analytics |
| `/api/metrics/activity/stream` | Real-time activity (WS) |
| `/api/settings` | App configuration |
| `/api/jobs` | Background job tracking |
| `/api/performance` | Performance stats |
| `/api/health` | Health check |

## Configuration

### Settings (`config/settings.yaml`)

```yaml
llm:
  model: claude-sonnet-4-20250514
  max_tokens: 4096
  temperature: 0.7

rag:
  embedding_model: all-MiniLM-L6-v2
  chunk_size: 512
  top_k: 5
  similarity_threshold: 0.3

mcp:
  enabled_servers:
    - filesystem
    - web_search
    - github
    - browser
    - web_fetch
    - docgen
    - realtime_data
    - calculator
    - llm_chat

personality:
  name: "Twin"
  role: "personal AI assistant and digital twin"
  tone: "professional but friendly"
```

### Personality (`config/prompts/personality.yaml`)

Customize your twin's name, traits, and behavior through the personality configuration file.

## Deployment

### Railway (Backend)

1. Push to GitHub
2. Connect your Railway project
3. Set environment variables (`ANTHROPIC_API_KEY`, etc.)
4. Deploy — Railway auto-detects the Python app

### Vercel (Frontend)

1. Connect your GitHub repo to Vercel
2. Set build command: `cd frontend && npm run build`
3. Set output directory: `frontend/dist`
4. Add `BACKEND_URL` environment variable pointing to your Railway deployment

## Project Structure

```
twinbot/
├── backend/
│   ├── main.py              # FastAPI app factory
│   ├── config.py             # Settings from environment
│   ├── routers/              # API route handlers
│   ├── services/             # Business logic layer
│   ├── models/               # SQLAlchemy ORM + Pydantic schemas
│   ├── integrations/         # Sentry, Supabase, guardrails
│   ├── utils/                # Logging, errors, RBAC, caching
│   └── websocket/            # WebSocket connection management
├── frontend/
│   └── src/
│       ├── pages/            # Dashboard, Chat, Agents, RAG, etc.
│       ├── components/       # Sidebar, Header, PageWrapper
│       ├── services/         # API client
│       ├── hooks/            # Custom React hooks
│       └── store/            # Zustand state management
├── src/twinbot/              # Core agent library
│   ├── agents/               # Agent type implementations
│   ├── tools/                # MCP tool registry
│   ├── memory/               # Memory subsystem
│   └── orchestrator/         # Agent routing
├── config/                   # YAML settings + prompt templates
├── infrastructure/           # Supabase schema
├── data/                     # Local data (ChromaDB, logs, uploads)
├── scripts/                  # Deployment & setup utilities
├── launcher.py               # One-click Windows launcher
├── docker-compose.yml        # Container orchestration
├── Dockerfile                # Multi-stage build
└── pyproject.toml            # Python package config
```

## License

All rights reserved.
