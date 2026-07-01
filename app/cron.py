"""Cron helpers — read CRON_SCHEDULE env and compute next run."""
from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Optional

try:
    from croniter import croniter
except ImportError:
    croniter = None


DEFAULT_CRON = "0 6 * * *"


def get_schedule() -> str:
    return os.environ.get("CRON_SCHEDULE", DEFAULT_CRON)


def next_run(now: Optional[datetime] = None) -> Optional[datetime]:
    if croniter is None:
        return None
    base = now or datetime.now(timezone.utc)
    return croniter(get_schedule(), base).get_next(datetime)
