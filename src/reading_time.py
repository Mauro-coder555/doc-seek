"""Reading time and reading speed utilities for Doc Seek."""

from datetime import datetime
from typing import Any


DEFAULT_WPM = 220


def estimate_reading_minutes(word_count: int, average_wpm: float | None = None) -> int:
    """Estimate reading time in minutes."""
    if word_count <= 0:
        return 0

    wpm = average_wpm or DEFAULT_WPM
    minutes = word_count / wpm

    return max(1, round(minutes))


def get_average_wpm(stats: dict[str, Any]) -> float | None:
    """Return the stored average words per minute."""
    average_wpm = stats.get("average_wpm")

    if average_wpm is None:
        return None

    try:
        return float(average_wpm)
    except (TypeError, ValueError):
        return None


def add_reading_session(
    stats: dict[str, Any],
    document_title: str,
    word_count: int,
    elapsed_seconds: float,
) -> dict[str, Any]:
    """Add a reading session and update average WPM."""
    if elapsed_seconds <= 0 or word_count <= 0:
        return stats

    elapsed_minutes = elapsed_seconds / 60
    session_wpm = word_count / elapsed_minutes

    sessions = stats.get("reading_sessions", [])

    sessions.append(
        {
            "document_title": document_title,
            "word_count": word_count,
            "elapsed_seconds": round(elapsed_seconds, 2),
            "wpm": round(session_wpm, 2),
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
    )

    average_wpm = sum(session["wpm"] for session in sessions) / len(sessions)

    stats["reading_sessions"] = sessions
    stats["average_wpm"] = round(average_wpm, 2)

    return stats