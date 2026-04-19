"""Centralized path constants for the writing2 project."""
from __future__ import annotations

from pathlib import Path

# Repository root where source code lives.
REPO_ROOT: Path = Path("/mnt/r/writing2")

# Shared local serving-stack repository used for model metadata.
CONNECTIONS_ROOT: Path = Path("/mnt/r/connections")

# External data directory that holds large artifacts (stories, grades, etc.).
DATA_ROOT: Path = Path("/mnt/r/writing2-data")


def data_subdir(name: str) -> Path:
    """Return the full path to a named data subdirectory under ``DATA_ROOT``."""
    return DATA_ROOT / name


__all__ = ["REPO_ROOT", "CONNECTIONS_ROOT", "DATA_ROOT", "data_subdir"]
