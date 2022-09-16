class FreqStack:

    def __init__(self):
        self.time = 0
        self.freq = collections.defaultdict(int)
        self.heap = []
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.heap, (-self.freq[val], -self.time, val))
        self.time += 1
        
    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()