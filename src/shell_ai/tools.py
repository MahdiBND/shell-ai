from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from langchain_core.tools import tool


@tool
def get_current_time(timezone: str = "UTC") -> str:
    """Get the current date, weekday and time in a timezone.

    Args:
        timezone: IANA timezone name, e.g. "UTC", "Europe/Oslo", "America/New_York".
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError, ValueError:
        return (
            f"ERROR: unknown timezone '{timezone}'. "
            "Use an IANA name like 'Europe/London' or 'Asia/Tokyo'."
        )
    return now.strftime(f"%A, %Y-%m-%d, %H:%M:%S ({timezone}, UTC%z)")
