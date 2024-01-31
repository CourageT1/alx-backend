#!/usr/bin/python3
"""a class LIFOCache that inherits from BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defines the LIFOCache class """

    def __init__(self):
        """ Initializes the LIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using LIFO algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
