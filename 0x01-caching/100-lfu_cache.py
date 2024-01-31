#!/usr/bin/env python3
"""a class LFUCache that inherits from BaseCaching and is a caching system"""

from collections import defaultdict
from functools import cmp_to_key

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Defines the LFUCache class """

    def __init__(self):
        """ Initializes the LFUCache instance """
        super().__init__()
        self.frequency = defaultdict(int)
        self.order_used = []

    def put(self, key, item):
        """ Adds an item to the cache using LFU algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._discard_least_frequent()
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order_used.append(key)

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is not None and key in self.cache_data:
            # Update frequency and order_used list
            self.frequency[key] += 1
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None

    def _discard_least_frequent(self):
        """ Discards the least frequent used item(s) """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [key for key, freq in self.frequency.items(
            ) if freq == min_frequency]
        if len(least_frequent_keys) == 1:
            discarded_key = least_frequent_keys[0]
        else:
            discarded_key = min(
                    least_frequent_keys, key=lambda k:
                    self.order_used.index(k)
                    )
        del self.cache_data[discarded_key]
        del self.frequency[discarded_key]
        self.order_used.remove(discarded_key)
        print(f"DISCARD: {discarded_key}")

    def print_cache(self):
        """ Prints the cache with LFU order """
        print("Current cache:")
        for key in sorted(
                self.cache_data,
                key=cmp_to_key(lambda x, y: self._compare(x, y))
                ):
            print(f"{key}: {self.cache_data[key]}")
        print()

    def _compare(self, x, y):
        """ Custom comparison function to sort keys based on frequency
        and order_used """
        if self.frequency[x] != self.frequency[y]:
            return self.frequency[x] - self.frequency[y]
        return self.order_used.index(y) - self.order_used.index(x)
