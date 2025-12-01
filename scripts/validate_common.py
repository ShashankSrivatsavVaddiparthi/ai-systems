# ruff: noqa: E402
import sys
import traceback
from importlib import import_module
from pathlib import Path

# Add repo root to sys.path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Import logger AFTER sys.path is updated
from common.logging.logger import logger

modules = [
    "common.logging.logger",
    "common.config",
    "common.helpers",
    "common.data",
]

errors = []

logger.info("Running quick common-layer validation...")

for m in modules:
    try:
        mod = import_module(m)
        logger.info(f"OK  import {m}")
    except Exception as e:
        errors.append((m, e, traceback.format_exc()))
        logger.error(f"ERR import {m}: {e}")

# quick function checks
try:
    from common.config import get_settings

    s = get_settings()
    logger.info(f"OK  get_settings -> {s}")
except Exception as e:
    errors.append(("get_settings", e, traceback.format_exc()))
    logger.error(f"ERR get_settings: {e}")

try:
    from common.helpers import current_timestamp

    logger.info(f"OK  helpers -> timestamp: {current_timestamp()}")
except Exception as e:
    errors.append(("helpers", e, traceback.format_exc()))
    logger.error(f"ERR helpers: {e}")

try:
    from common.data import clean_text

    logger.info(f"OK  data -> clean_text: {clean_text('  hello   world ')}")
except Exception as e:
    errors.append(("data", e, traceback.format_exc()))
    logger.error(f"ERR data: {e}")

if errors:
    logger.error("Validation completed with errors:")
    for name, exc, tb in errors:
        logger.error(f"- {name}: {exc}")
        logger.error(tb)
    sys.exit(2)
else:
    logger.info("Validation OK — common layer looks importable.")
    sys.exit(0)
