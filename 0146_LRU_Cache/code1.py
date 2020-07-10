class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key = collections.deque()
        self.value = collections.defaultdict(int)
        

    def get(self, key: int) -> int:
        ans = self.value[key] + (self.value[key] == 0) * (-1)
        if(ans != -1):
            self.key.remove(key)
            self.key.appendleft(key)
        return ans
        

    def put(self, key: int, value: int) -> None:
        if(key not in self.key):
            if(len(self.key) == self.capacity):
                del self.value[self.key.pop()]
            self.value[key] = value
            self.key.appendleft(key)
        else:
            self.key.remove(key)
            self.key.appendleft(key)      
            self.value[key] = value