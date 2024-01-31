#!/usr/bin/python3
"""a class FIFOCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defines the FIFOCache class """

    def __init__(self):
        """ Initializes the FIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using FIFO algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
