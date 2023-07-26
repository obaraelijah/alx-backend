#!/usr/bin/env python3
"""Basic caching module Task"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing in a dict"""
    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        
    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)
