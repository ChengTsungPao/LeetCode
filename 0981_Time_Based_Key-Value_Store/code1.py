class TimeMap:

    def __init__(self):
        self.value = collections.defaultdict(list)
        self.timestamp = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value[key].append(value)
        self.timestamp[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect_left(self.timestamp[key], timestamp)
        index -= index >= len(self.timestamp[key]) or self.timestamp[key][index] != timestamp
        
        if index >= 0:
            return self.value[key][index]
        else:
            return ""
        
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)