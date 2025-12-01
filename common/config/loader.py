from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv


def load_yaml_config(path: str | Path) -> Dict[str, Any]:
    """
    Load a YAML configuration file and return it as a dictionary.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_environment_variables(env_path: str | Path | None = None) -> None:
    """
    Load environment variables from a .env file.
    """
    if env_path is None:
        load_dotenv()
    else:
        load_dotenv(dotenv_path=env_path)
