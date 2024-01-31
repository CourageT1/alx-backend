#!/usr/bin/python3
"""a class LRUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defines the LRUCache class """

    def __init__(self):
        """ Initializes the LRUCache instance """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Adds an item to the cache using LRU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order_used.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the order_used list
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Prints the cache with LRU order """
        print("Current cache:")
        for key in self.order_used:
            print(f"{key}: {self.cache_data[key]}")
        print()
