# PromptOps

PromptOps is a modular, LLM-powered laptop automation framework. It enables natural language automation of desktop tasks using skills, agents, and screen understanding.

## System Flow

- User Prompt → Main Agent → Task Planner → Skill Registry (Qdrant + Mongo) → Sequential Skill Execution → Laptop Actions
- Auto Skill Updater LLM generates new skills if needed
- All actions are logged and permission-checked

## Folder Structure

- `/agents`: LLM agents (working agent, task planner, skill updater)
- `/registry`: Skill Registry (Qdrant for vector similarity + MongoDB for metadata)
- `/skills`: Base and OS-level skill implementations
- `/execution`: Skill execution engine
- `/vision`: Screen capture + OCR + UI state analysis
- `/llm`: LLM clients and embedder
- `/memory`: Logs, traces, skill usage history
- `/web`: (optional) FastAPI + Next.js frontend

## Quickstart

1. Install requirements: `pip install -r requirements.txt`
2. Run: `python main.py`
3. Enter a prompt (e.g., "Click the OK button")

## Features

- Modular async agents and skills
- Qdrant + MongoDB skill registry
- Auto skill generation with Gemini/OpenAI
- Screen understanding with OCR
- Permission-aware execution
- Full logging and traceability
