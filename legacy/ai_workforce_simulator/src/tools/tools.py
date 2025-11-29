from langchain.tools import tool
from e2b_code_interpreter import Sandbox
import os
import sys
from tools.tool_schemas import CodeToolParams, WriteFileParams

@tool(args_schema=CodeToolParams)
def code_tool(code: str, language: str = "python"):
    """Execute code in a sandboxed environment and return the output or error.

    Args are validated against CodeToolParams when available (pydantic model).
    """
    sbx = Sandbox.create()
    # run_code may accept language as an option depending on implementation; include it if supported
    try:
        execution = sbx.run_code(code, language=language)
    except TypeError:
        # fallback if sandbox.run_code only accepts a single argument
        execution = sbx.run_code(code)
    if execution.error:
        return f"Error: {execution.error}"
    return execution.results

@tool(args_schema=WriteFileParams)
def write_file(filename: str, content: str) -> str:
    """Unified file-write tool. Use this tool to create documentation or code files.

    Arguments are validated against WriteFileParams when pydantic is available.

    Writes `content` to `src/output/<filename>` creating parent directories as needed.
    Returns a single-line status message with the absolute path.
    """
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "output")
    file_path = os.path.join(output_dir, filename)
    parent = os.path.dirname(file_path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    msg = f"File written to {file_path} (cwd={os.getcwd()}, sys.path[0]={sys.path[0]})"
    print(msg, flush=True)
    return msg
