#!/usr/bin/python3
"""  a class BasicCache that inherits from BaseCaching and
is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defines the BasicCache class """

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
