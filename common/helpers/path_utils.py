from pathlib import Path
from typing import Union


def ensure_dir(path: Union[str, Path]) -> Path:
    """
    Ensure a directory exists. If it doesn't, create it.
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def project_root() -> Path:
    """
    Return the project root directory (monorepo root).
    """
    return Path(__file__).resolve().parent.parent.parent


def resolve_path(path: Union[str, Path]) -> Path:
    """
    Convert to am absolute Path object.
    """
    return Path(path).expanduser().resolve()
