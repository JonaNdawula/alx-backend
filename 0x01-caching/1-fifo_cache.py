#!/usr/bin/env python3
"""
Module contains FIFOCache class which
inherits from BaseCaching and is
a caching system, The
class is a FiFO cache system
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from
    the BaseCaching, The class uses a
    FIFO cache system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        put Items into cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded = self.keys.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data
        """
        return self.cahce_data.get(key, None)
