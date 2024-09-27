import streamlit as st
from functools import wraps
import redis
from config import REDIS_HOST, REDIS_PORT

# 创建Redis连接
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def cache_data(ttl=3600):
    """
    缓存装饰器，用于缓存函数返回的数据
    :param ttl: 缓存过期时间（秒），默认1小时
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # 尝试从Redis获取缓存数据
            cached_data = redis_client.get(cache_key)
            if cached_data:
                return st.json.loads(cached_data)
            
            # 如果没有缓存，执行函数并缓存结果
            result = func(*args, **kwargs)
            redis_client.setex(cache_key, ttl, st.json.dumps(result))
            return result
        return wrapper
    return decorator

def clear_cache(key_pattern="*"):
    """
    清除指定模式的缓存
    :param key_pattern: Redis键模式，默认清除所有缓存
    """
    for key in redis_client.scan_iter(key_pattern):
        redis_client.delete(key)

def get_cache_size():
    """
    获取当前缓存大小
    :return: 缓存大小（字节）
    """
    return redis_client.info()["used_memory"]
