from datetime import datetime


def validate_date_range(from_date: datetime, to_date: datetime) -> bool:
    return from_date < to_date
