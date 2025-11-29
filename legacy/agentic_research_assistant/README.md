# Agentic Research Assistant

An intelligent research assistant powered by multiple specialized AI agents working together to help with complex research tasks.

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/SamSrivat/agentic_research_assistant)

## Overview

The Agentic Research Assistant is a sophisticated multi-agent system designed to help with research tasks by combining different capabilities like web search, document analysis, and database querying. It uses a supervisor agent architecture to coordinate multiple specialized agents for different tasks.

## Features

### Current Capabilities

- **Supervisor Assistant Agent**: Coordinates all other agents and manages user interactions
- **Web Search Agent**: Performs intelligent web searches to gather information
- **Document RAG Agent**: 
  - Processes and retrieves information from web documents
  - Handles PDF document analysis
  - Implements RAG (Retrieval Augmented Generation) for accurate information retrieval
- **SQL Agent**: Queries and analyzes data from user-provided databases
- **Gradio Web Interface**: Simple and intuitive user interface for interaction

### Upcoming Features

- Memory system for contextual conversations
- Documentation agent for structured output
- Microsoft Word (docx) document processing
- Code analysis and generation capabilities

## Technology Stack

- **Core Framework**: LangChain & LangGraph
- **Vector Store**: FAISS
- **Document Processing**: PyMuPDF
- **Web Interface**: Gradio
- **Additional Libraries**:
  - sentence-transformers
  - langchain-supervisor
  - langchain-tavily
  - langchain-groq
  - langchain-huggingface
  - Beautiful Soup (bs4)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShashankSrivatsavVaddiparthi/agentic-research-assistant.git
   cd agentic-research-assistant
   ```

2. Install dependencies (Option 1 - using pip):
   ```bash
   pip install -r requirements.txt
   ```
   
   OR (Option 2 - using uv, recommended):
   ```bash
   uv pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys and configurations in `.env`

## Usage

1. Start the application:
   ```bash
   # Using standard Python
   python src/app.py
   
   # Or using uv
   uv run python src/app.py
   ```

2. Open the Gradio interface in your browser (typically at http://localhost:7860)

3. Enter your research query in the text input

## System Architecture

### Workflow

1. User interacts with the Assistant (Supervisor Agent)
2. Assistant analyzes the query and delegates tasks to specialized agents:
   - Web Search Agent for internet research
   - Document RAG Agent for document analysis
   - SQL Agent for database queries
3. Agents process their tasks and return results
4. Assistant synthesizes information and provides a coherent response

### Agent Roles

- **Assistant Agent**: Supervises and coordinates all other agents
- **Web Search Agent**: Performs targeted internet searches
- **Document RAG Agent**: Processes and analyzes documents
- **SQL Agent**: Handles database interactions and queries

## Demo

Try out the live demo on Hugging Face Spaces: [Agentic Research Assistant](https://huggingface.co/spaces/SamSrivat/agentic_research_assistant)

## Project Structure
```
src/
├── app.py              # Main application entry point
├── main.py            # Core application logic
├── agents/            # Agent implementations
│   ├── assistant_agent.py
│   ├── retrieval_agent.py
│   ├── sql_agent.py
│   └── web_search_agent.py
├── tools/             # Agent tools and utilities
│   ├── retrieval_tools.py
│   ├── sql_tools.py
│   └── web_search_tools.py
└── utils/             # Helper functions and utilities
    ├── helpers.py
    ├── llm.py
    ├── prompts.py
    ├── sql_database.py
    └── vectorstore.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

_Note: This is an active research project, and features are being added regularly._
