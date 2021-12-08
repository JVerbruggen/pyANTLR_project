class Cache:
    def __init__(self):
        self.cache = dict()
    
    def push(self, key, val):
        if key is None: return
        self.cache[key] = val
    
    def pop(self):
        if len(self.cache) == 0: return None
        key = list(self.cache.keys())[-1]
        value = self.cache[key]
        del self.cache[key]
        return value

    def next(self, remove=True):
        if len(self.cache) == 0: return None

        cache_item = next(iter(self.cache))
        value = self.cache[cache_item]
        
        if remove:
            del self.cache[cache_item]
        return value
    
    def remove(self, key):
        if key not in self.cache: return
        del self.cache[key]

    def value(self, key):
        if key not in self.cache: return None
        return self.cache[key]

    def __str__(self):
        return str(self.cache)