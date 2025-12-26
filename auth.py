from fastapi import Header, HTTPException
from config import API_KEYS_FREE, API_KEYS_PRO
from rate_limit import check_rate_limit

def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API Key gerekli")

    if x_api_key in API_KEYS_PRO:
        return {"key": x_api_key, "plan": "pro"}

    if x_api_key in API_KEYS_FREE:
        limit_info = check_rate_limit(x_api_key, is_pro=False)
        return {"key": x_api_key, "plan": "free", **limit_info}

    raise HTTPException(status_code=401, detail="Geçersiz API Key")