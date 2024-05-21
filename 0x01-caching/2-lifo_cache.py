#!/usr/bin/env python3
"""
This module contains The LIFOCache class
which inherits from the BaseCaching and
is a caching system. Its a
lifo Cache System
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from
    the BaseCaching. The class use a
    LIFO cache System
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Put items into cache
        """
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
        Returns the value in
        self.cache_data
        """
        return self.cache_data.get(key, None)
