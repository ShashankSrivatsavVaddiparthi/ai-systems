import sys
from pathlib import Path

from loguru import logger


def _create_log_directory(path: Path) -> None:
    """Ensure the log directory exists."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def configure_logger(
    log_level: str = "INFO",
    log_to_file: bool = True,
    log_dir: str = "logs",
    log_filename: str = "app.log",
) -> None:
    """
    Configure the Loguru logger for use across the monorepo.

    Args:
        log_level (str): Logging level (INFO, DEBUG, WARNING, ERROR)
        log_to_file (bool): Whether to save logs to a file
        log_dir (str): Directory where log files will be saved
        log_filename (str): Log file name
    """

    # Remove default logger
    logger.remove()

    # Console output handler
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>",
    )

    # Optional file output
    if log_to_file:
        log_path = Path(log_dir)
        _create_log_directory(log_path)

        logger.add(
            log_path / log_filename,
            rotation="5 MB",
            retention="10 days",
            level=log_level,
            compression="zip",
            enqueue=True,
            encoding="utf-8",
        )

    logger.debug("Logger initialized.")


# Automatically initialize logger (default settings)
configure_logger()

__all__ = ["logger", "configure_logger"]
