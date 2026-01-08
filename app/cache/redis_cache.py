import json
import redis
from app.core.config import settings
from app.utils.json_utils import make_json_safe


redis_client = redis.Redis.from_url(settings.REDIS_URL)


def get_cache_prediction(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache_prediction(key: str, value, expiry: int = 3600):
    safe_value = make_json_safe(value)
    redis_client.setex(key, expiry, json.dumps(safe_value))
