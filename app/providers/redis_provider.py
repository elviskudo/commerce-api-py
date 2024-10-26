import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_client = redis.Redis.from_url(REDIS_URL)

# Contoh penggunaan Redis
def cache_data(key: str, value: str):
    redis_client.set(key, value)

def get_cached_data(key: str):
    return redis_client.get(key)