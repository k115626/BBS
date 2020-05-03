from redis import Redis
import pickle


cache = Redis(host='127.0.0.1', port=6379)


def set(key, val, timeout=60):
    val = pickle.dumps(val)
    return cache.setex(key, timeout, val)


def get(key):
    val = cache.get(key)
    if val:
        return pickle.loads(val)
    else:
        return None


def delete(key):
    return cache.delete(key)
