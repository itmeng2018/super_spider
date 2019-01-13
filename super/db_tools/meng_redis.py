import redis

def _retry(function):
    def decorate(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception:
            result = None
        return result
    return decorate


class RedisHelper(object):
    def __init__(self, name=None):
        self.__conn = redis.Redis(host='139.196.137.234', port=6379, )
        self.name = name or 'meng'

    def push_list(self, *msg, direction='left'):
        if direction == 'right':
            self.__conn.rpush(self.name, *msg)
        else:
            self.__conn.lpush(self.name, *msg)

    @_retry
    def get_list(self, start, end):
        result_list = self.__conn.lrange(self.name, start, end)
        for item in result_list:
            yield item.decode()

    @_retry
    def get_list_len(self):
        return self.__conn.llen(self.name)

    @_retry
    def pop_list(self, direction='left'):
        if direction == 'right':
            return self.__conn.rpop(self.name).decode()
        return self.__conn.lpop(self.name).decode()

    def delete_list(self):
        self.__conn.delete(self.name)

    def set(self, name, value):
        self.__conn.set(name, value)

    @_retry
    def get(self, name):
        return self.__conn.get(name).decode()