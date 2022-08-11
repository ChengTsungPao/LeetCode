class MaxStack:

    def __init__(self):
        self.exist = set()
        self.stack = []
        self.heap  = []
        self.id = 0

    def push(self, x: int) -> None:
        self.exist.add(self.id)
        self.stack.append((x, self.id))
        heapq.heappush(self.heap, (-x, -self.id))
        self.id += 1
        
    def pop(self) -> int:
        val, prevID = self.stack.pop()
        while prevID not in self.exist:
            val, prevID = self.stack.pop()
        self.exist.remove(prevID)
        return val

    def top(self) -> int:
        while self.stack[-1][1] not in self.exist:
            val, prevID = self.stack.pop()
        val, prevID = self.stack[-1]
        return val
        
    def peekMax(self) -> int:
        while -self.heap[0][1] not in self.exist:
            val, prevID = heapq.heappop(self.heap)
        val, prevID = self.heap[0]
        return -val

    def popMax(self) -> int:
        val, prevID = heapq.heappop(self.heap)
        while -prevID not in self.exist:
            val, prevID = heapq.heappop(self.heap)
        self.exist.remove(-prevID)
        return -val        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()