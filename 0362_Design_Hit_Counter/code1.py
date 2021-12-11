class HitCounter:

    def __init__(self):
        self.que = collections.deque()
        
    def adjust(self, currentTime: int):
        while self.que and currentTime - self.que[-1] >= 300:
            self.que.pop()

    def hit(self, timestamp: int) -> None:
        self.que.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.adjust(timestamp)
        return len(self.que)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)