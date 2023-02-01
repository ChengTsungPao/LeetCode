class HitCounter:

    def __init__(self):
        self.que = collections.deque()
        
    def adjust(self, timestamp):
        while self.que and timestamp - self.que[0] + 1 > 300:
            self.que.popleft()

    def hit(self, timestamp: int) -> None:
        self.adjust(timestamp)
        self.que.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        self.adjust(timestamp)
        return len(self.que)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)