#!/usr/bin/env python3
''' contains cache class '''


import uuid
import redis
from typing import Union


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
