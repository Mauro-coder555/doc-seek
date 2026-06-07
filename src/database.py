"""Local JSON storage utilities for Doc Seek."""

import json
from pathlib import Path
from typing import Any


DATA_DIR = Path("data")
METADATA_FILE = DATA_DIR / "metadata.json"
READING_STATS_FILE = DATA_DIR / "reading_stats.json"


DEFAULT_METADATA = {
    "documents": []
}

DEFAULT_READING_STATS = {
    "reading_sessions": [],
    "average_wpm": None
}


def ensure_data_files() -> None:
    """Create the data directory and required JSON files if they do not exist."""
    DATA_DIR.mkdir(exist_ok=True)

    if not METADATA_FILE.exists():
        write_json(METADATA_FILE, DEFAULT_METADATA)

    if not READING_STATS_FILE.exists():
        write_json(READING_STATS_FILE, DEFAULT_READING_STATS)


def read_json(file_path: Path, default: dict[str, Any]) -> dict[str, Any]:
    """Read a JSON file safely."""
    if not file_path.exists():
        return default

    try:
        content = file_path.read_text(encoding="utf-8").strip()

        if not content:
            return default

        data = json.loads(content)

        if not isinstance(data, dict):
            return default

        return data

    except json.JSONDecodeError:
        return default


def write_json(file_path: Path, data: dict[str, Any]) -> None:
    """Write data to a JSON file."""
    file_path.parent.mkdir(exist_ok=True)

    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_metadata() -> dict[str, Any]:
    """Load document metadata."""
    ensure_data_files()
    return read_json(METADATA_FILE, DEFAULT_METADATA)


def save_metadata(metadata: dict[str, Any]) -> None:
    """Save document metadata."""
    write_json(METADATA_FILE, metadata)


def load_reading_stats() -> dict[str, Any]:
    """Load reading statistics."""
    ensure_data_files()
    return read_json(READING_STATS_FILE, DEFAULT_READING_STATS)


def save_reading_stats(stats: dict[str, Any]) -> None:
    """Save reading statistics."""
    write_json(READING_STATS_FILE, stats)