class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if(key in self.cache):
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if(key not in self.cache):
            if(len(self.cache) == self.capacity):
                self.cache.popitem(last=True)
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)