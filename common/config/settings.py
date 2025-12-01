from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from .loader import load_environment_variables, load_yaml_config


class AppSettings(BaseModel):
    """
    Main settings model for the monorepo.
    Extend this as needed for all projects.
    """

    # Example global settings
    environment: str = Field(default="development")
    debug: bool = Field(default=False)

    # Logging settings
    log_level: str = Field(default="INFO")
    log_to_file: bool = Field(default=True)


def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively merge two dictionaries.
    Values in 'override' take precedence
    """
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


@lru_cache()
def get_settings(config_path: Optional[str | Path] = None) -> AppSettings:
    """
    Load settings from:
    1. Environment variables (.env)
    2. YAML configuration file (optional)
    3. Defaults in AppSettings model

    Settings are cached so loading happens only once.
    """

    # Load .env first
    load_environment_variables()

    data: Dict[str, Any] = {}

    # Load YAML configuration if provided
    if config_path:
        yaml_data = load_yaml_config(config_path)
        data = merge_dicts(data, yaml_data)

    return AppSettings(**data)
