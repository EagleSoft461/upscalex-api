from datetime import datetime, date
from fastapi import HTTPException

usage_store = {}
FREE_DAILY_LIMIT = 10

def check_rate_limit(api_key: str, is_pro: bool):
    if is_pro:
        return {"remaining": None, "limit": None}
    
    today = date.today()

    if api_key not in usage_store or usage_store[api_key]["date"] != today:
        usage_store[api_key] = {"date": today, "count": 0}

    if usage_store[api_key]["count"] >= FREE_DAILY_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Günlük ücretsiz limit doldu"
        )

    usage_store[api_key]["count"] += 1

    remaining = FREE_DAILY_LIMIT - usage_store[api_key]["count"]

    return {
        "limit": FREE_DAILY_LIMIT,
        "remaining": remaining
    }