"""Фильтр алертов: из списка событий оставляем только критичные."""

import json
from pathlib import Path
import sys

CRITICAL = "critical"


def is_critical(event: dict) -> bool:
    """Событие критично, если его уровень — critical (регистр не важен)."""
    return str(event.get("level", "")).strip().lower() == CRITICAL


def main() -> None:
    # Не падать в Windows-консоли с локальной кодировкой cp1251.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    events_path = Path(__file__).with_name("events.json")
    events = json.loads(events_path.read_text(encoding="utf-8"))

    critical_events = [event for event in events if is_critical(event)]

    for event in critical_events:
        print(f"[{event['level'].upper()}] {event['service']}: {event['message']}")

    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()
