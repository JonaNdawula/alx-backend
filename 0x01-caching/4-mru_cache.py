#!/usr/bin/env python3
"""
This module contains MRUCache
class which inherits from BaseCaching
and is a caching system. The class
is a MRU cache system
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from
    the BaseCaching. The class uses as
    MRU cache system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        put items into cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded = self.keys.pop()
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
