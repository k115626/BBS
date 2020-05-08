import pickle
from redis import Redis as _Redis
from bbs.config import REDIS


class Redis(_Redis):

    def get(self, name):
        pickle_value = super().get(name)
        if pickle_value is None:
            return None
        else:
            try:
                value = pickle.loads(pickle_value)
            except pickle.UnpicklingError:
                return pickle_value
            else:
                return value

    def set(self, name, value, ex=60, px=None, nx=False, xx=False, keepttl=False):
        pickle_value = pickle.dumps(value, pickle.HIGHEST_PROTOCOL)
        return super().set(name, pickle_value, ex, px, nx, xx, keepttl)


rds = Redis(**REDIS)