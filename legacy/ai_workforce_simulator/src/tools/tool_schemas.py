from typing import TypedDict, Literal, Dict, Any


class CodeToolSchema(TypedDict):
    """TypedDict representing the high-level tool descriptor used by the agent framework.

    Note: most agent frameworks (OpenAI function calling / LangChain tools) expect a tool
    to expose a JSON Schema under the `parameters` key. We represent that here as a
    plain Dict[str, Any] containing a JSON Schema.
    """

    name: Literal["code_tool"]
    description: str
    parameters: Dict[str, Any]


# Example JSON Schema for the `code_tool` parameters. This is the schema that the
# model/agent should validate against. It requires a single `code` string field.
CODE_TOOL_JSON_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "title": "Code execution input",
    "properties": {
        "code": {
            "type": "string",
            "description": "The source code to execute in the sandboxed environment."
        },
        "language": {
            "type": "string",
            "description": "Optional: language identifier (e.g. 'python', 'javascript').",
            "default": "python"
        }
    },
    "required": ["code"],
    "additionalProperties": False,
}


# Example tool descriptor that you can pass to the agent framework for the code tool.
DEFAULT_CODE_TOOL: CodeToolSchema = {
    "name": "code_tool",
    "description": "Execute code in a sandbox and return the output or error.",
    "parameters": CODE_TOOL_JSON_SCHEMA,
}


# Example JSON Schema for the unified write_file tool. This expects a filename and
# the file content as strings. You can extend this schema (e.g., accept a `binary`
# flag or `encoding`) if needed.
WRITE_FILE_JSON_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "title": "Write file request",
    "properties": {
        "filename": {
            "type": "string",
            "description": "The target filename (relative to project output directory)."
        },
        "content": {
            "type": "string",
            "description": "File content to write (text)."
        }
    },
    "required": ["filename", "content"],
    "additionalProperties": False,
}


DEFAULT_WRITE_FILE_TOOL: Dict[str, Any] = {
    "name": "write_file",
    "description": "Write a file to the project's output folder.",
    "parameters": WRITE_FILE_JSON_SCHEMA,
}


# Convenience: examples of valid payloads (Python dicts) that will pass JSON Schema
# validation for each tool. Use these to test/validate before calling the agent.
EXAMPLE_CODE_TOOL_PAYLOAD: Dict[str, Any] = {"code": "print('hello world')", "language": "python"}
EXAMPLE_WRITE_FILE_PAYLOAD: Dict[str, Any] = {"filename": "index.html", "content": "<h1>Hello</h1>"}


# Pydantic models for use with LangChain's tool args_schema (recommended)
try:
    from pydantic import BaseModel, Field
    from typing import Optional

    class CodeToolParams(BaseModel):
        """Parameters accepted by the `code_tool` when called by the agent."""

        code: str = Field(..., description="The source code to execute in the sandboxed environment.")
        language: Optional[str] = Field("python", description="Optional language identifier (e.g. 'python').")

    class WriteFileParams(BaseModel):
        """Parameters accepted by the `write_file` tool."""

        filename: str = Field(..., description="Target filename relative to the project's output directory.")
        content: str = Field(..., description="Text content to write to the file.")

except Exception:
    # If pydantic isn't installed in the environment, provide placeholders so imports won't fail.
    CodeToolParams = None  # type: ignore
    WriteFileParams = None  # type: ignore
