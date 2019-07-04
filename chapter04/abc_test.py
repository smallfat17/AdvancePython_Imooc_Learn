from abc import abstractmethod,ABC,ABCMeta
from collections import abc

class CacheBase(metaclass=ABCMeta):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self):
        pass

class RedisCache(CacheBase):
    def get(self):
        pass

rc = RedisCache()
rc.get()

