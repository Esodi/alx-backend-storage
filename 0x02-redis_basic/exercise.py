#!/usr/bin/env python3
''' contains cache class '''


import uuid
import redis
from typing import Union, Type


class Cache:
    def __init__(self):
        ''' init method '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' converts to string '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key):
        v = self._redis.get(key)
        value = str(v)
        return value

    def get_int(self, key):
        v = self._redis.get(key)
        value = int(v)
        return value

    def get(self, key, fn: Type = None):
        ''' getter function '''
        if not key:
            return '(nil)'
        r = self._redis.get(key)
        if fn:
            return fn(r)
        return r
