import json
from pathlib import Path
from typing import Any, Dict, Iterable, Union


def read_jsonl(path: Union[str, Path]) -> Iterable[Dict[str, Any]]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: Union[str, Path], records: Iterable[Dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
