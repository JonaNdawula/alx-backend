#!/usr/bin/env python3
"""
A class BasicCache inheriting from
the BaseCaching class and is A
caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    inherits from BaseCaching class
    """

    def put(self, key, item):
        """
        put function for basic caching
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get function for basic caching
        """
        return self.cache_data.get(key, None)
