#!/usr/bin/env python3
"""a class MRUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """ Defines the MRUCache class """

    def __init__(self):
        """ Initializes the MRUCache instance """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Adds an item to the cache using MRU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order_used.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.order_used.insert(0, key)

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the beginning of the order_used list
            self.order_used.remove(key)
            self.order_used.insert(0, key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Prints the cache with MRU order """
        print("Current cache:")
        for key in self.order_used:
            print(f"{key}: {self.cache_data[key]}")
        print()
