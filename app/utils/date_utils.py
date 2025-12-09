"""Date and time utilities."""
from datetime import datetime
from typing import Optional


def parse_date(date_str: str) -> datetime:
    """Parse date string to datetime."""
    return datetime.fromisoformat(date_str)


def validate_date_range(from_date: datetime, to_date: datetime) -> bool:
    """Validate that from_date is before to_date."""
    return from_date < to_date


def check_date_range(start: datetime, end: datetime) -> bool:
    """Alternative date range validation."""
    if start >= end:
        return False
    return True
