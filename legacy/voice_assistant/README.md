**Voice Assistant (MVP)**

Lightweight voice assistant pipeline: STT (Whisper) → LLM (Groq) → TTS (Piper).

**Overview**

- **Purpose**: Provide HTTP and local UI interfaces that accept audio, transcribe it, query an LLM, and synthesize a spoken reply.
- **Components**: `src/stt.py`, `src/llm.py`, `src/tts.py`, `src/ui/gradio_app.py`, and FastAPI router glue in `src/routers.py`.

**Requirements**

- **Python**: `3.11.12` (see `pyproject.toml`).
- **Dependencies**: listed in `pyproject.toml` (install via `pip install .` or create a virtual env and `pip install -r requirements.txt` if you export one).

**Environment variables**
Update .env.example file with your GROQ_API_KEY and rename the file to .env

```
WHISPER_MODEL=small
GROQ_API_KEY=your_groq_api_key_here
PIPER_MODEL_PATH=path/to/en_US-lessac-medium.onnx
PIPER_CONFIG_PATH=path/to/en_US-lessac-medium.onnx.json
# Optionally override other settings
```

**Setup**

```
uv sync
```

**Install (PowerShell)**

- Create and activate a venv:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

- Install the project (uses `pyproject.toml`):

```powershell
python -m pip install --upgrade pip
python -m pip install .
```

Notes: packages such as `pyaudio`, `sounddevice`, or `soundfile` may need platform-specific system dependencies. Install them via your platform package manager if pip fails.

**Run — FastAPI (HTTP server)**

- Start the API server (from repo root):

```powershell
uvicorn src.main:app --reload --port 8000
```

- Health check: visit `http://127.0.0.1:8000/`.

**Run — Gradio UI (local)**

- Launch the simple Gradio demo (from repo root):

```powershell
python .\src\ui\gradio_app.py
```

**API Endpoints**

- **POST** `/transcribe` — multipart `audio_file` (file). Returns `{ timestamp, text, path }`.
- **POST** `/inference` — JSON or form `text` (string). Returns `{ timestamp, response, path }`.
- **POST** `/synthesize` — `text` (string). Returns `{ timestamp, path, audio_url }`.
- **POST** `/chat` — multipart `audio_file` (file). Runs full pipeline and returns paths and `audio_url`.

Example curl call (file upload):

```powershell
curl -X POST "http://127.0.0.1:8000/transcribe" -F "audio_file=@path\to\file.wav"
```

**Data layout**

- `data/input/audio` — incoming audio files saved by the API/UI.
- `data/input/text` — saved transcripts.
- `data/output/audio` — synthesized replies.
- `data/output/text` — LLM output text files.

**Notes**

- The project expects model artifacts (Piper ONNX files) in `models/piper` by default. Set `PIPER_MODEL_PATH`/`PIPER_CONFIG_PATH` to point to those files.

**Next steps**

- **Streaming**: add streaming support for STT, LLM, and TTS so the pipeline can operate with lower latency and partial results.
- **Memory**: implement short-term (session) and long-term memory stores to preserve context across turns and sessions.
- **Agentic capabilities**:

  - **RAG (Retrieval-Augmented Generation)**:
    - Local docs: index a local document store (files, PDFs, notes) for retrieval.
    - Google Drive: integrate Drive as a content source and index selected folders.
  - **Websearch**: add a safe websearch connector for real-time information and grounding.
  - **Email**: add read/send email capabilities (with user OAuth) for assistant-driven messaging.
  - **Calendar**: integrate calendar access (read/create events) for scheduling and reminders.
- **Other possible capabilities**:

  - Try different voice models.
  - Speaker diarization and identification for multi-speaker conversations.
  - Language detection and on-the-fly translation for multilingual conversations.
  - WebRTC or low-latency streaming for real-time voice assistants.
  - Authentication / user accounts and per-user data isolation.
  - Model management: dynamic model selection, versioning, and local fallback models.
  - Monitoring, logging, and metrics (latency, transcription quality, usage) for production readiness.
