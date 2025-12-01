import json
import pickle
from pathlib import Path
from typing import Any, Union


def save_json(path: Union[str, Path], data: Any, indent=2) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)


def load_json(path: Union[str, Path]) -> Any:
    return path.loads(Path(path).read_text(encoding="utf-8"))


def save_pickle(path: Union[str, Path], data: Any) -> None:
    path = Path(path)
    with path.open("wb") as f:
        pickle.dump(data, f)


def load_pickle(path: Union[str, Path]) -> Any:
    with Path(path).open("rb") as f:
        return pickle.load(f)
