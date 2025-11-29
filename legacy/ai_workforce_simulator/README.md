
# AI Workforce Simulator

A small experimental project that composes multiple LangChain/agent-style components to simulate an AI "workforce" (planner, developer, tester, reviewer, documenter) coordinated by a supervisor. The repository provides an example entrypoint that streams the supervisor's execution and demonstrates how agents can collaborate to complete a task.

## Key ideas

- Multiple small agents (planner, developer, tester, reviewer, documenter) each with a focused system prompt.
- A supervisor coordinates agent handoffs and composes the overall workflow.
- Tools (for example: code execution, file write) are exposed to specific agents.

This project is experimental and intended as a reference implementation / playground for agent orchestration patterns using LangChain and related tooling.

## Requirements

- Python 3.13+ (pyproject specifies >=3.13)
- See `pyproject.toml` and `requirements.txt` for details. Common dependencies include LangChain and helper libraries listed in the project metadata.

Recommended: create and use a virtual environment.

## Installation

1. Clone the repository:

```
git clone <repo-url>
cd ai_workforce_simulator
```

2. Create and activate a virtual environment (Windows PowerShell example):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Install dependencies (pip):

```powershell
pip install -r requirements.txt
# or use the pyproject/poetry tooling if you prefer
```

4. Create a `.env` file with any required API keys (provider-specific). This project uses LangChain-style LLM backends, so set the appropriate environment variables for your model provider (for example, OPENAI_API_KEY or GOOGLE_API_KEY depending on which LLM integration you use).

## Quick usage

The example entrypoint is `src/main.py`. It demonstrates running the supervisor with a simple payload and streaming the results.

Run it like this (PowerShell):

```powershell
python src\main.py
```

The script will call the `supervisor.stream(payload)` generator and pretty-print chunks as they arrive.

You can adapt the `payload` in `src/main.py` to try different tasks or messages.

## Project structure

- `src/main.py` - example entrypoint that runs a sample supervisor stream.
- `src/agents/agent_system_prompts.py` - system prompts and agent prompt definitions.
- `src/agents/agents.py` - agent creation and supervisor assembly.
- `src/tools/tool_schemas.py`, `src/tools/tools.py` - tool definitions and schemas exposed to agents.
- `src/utils/llms.py` - LLM configuration and helper functions.
- `src/utils/message_display.py` - pretty-print helpers used by the example.
- `requirements.txt` / `pyproject.toml` - dependency metadata.

## Configuration notes

- The `pyproject.toml` lists runtime dependencies and indicates Python 3.13+. Adjust as needed for your environment.
- The code imports `dotenv.load_dotenv()` in `src/main.py` so environment variables from a `.env` file will be loaded automatically.

Example `.env` (provider-specific):

```
# OPENAI_API_KEY=...
# GOOGLE_API_KEY=...
```

## Extending the project

- Add or modify agent prompts in `src/agents/agent_system_prompts.py`.
- Add new tools in `src/tools/tools.py` and expose them to specific agents when creating them in `src/agents/agents.py`.
- The supervisor is created with `create_supervisor(...).compile()` and returns an object with a `.stream(payload)` generator that yields progress chunks.

## Notes & caveats

- This project is experimental. Be careful with cost and safety when running real LLM calls.
- The exact environment variables and provider setup depend on which LangChain model integrations you choose to use (check `src/utils/llms.py`).

## Contributing

Contributions are welcome. Open an issue or PR with a clear description of the change. Keep changes small and test locally.

## License

Add your license here (e.g., MIT) or keep as placeholder.


