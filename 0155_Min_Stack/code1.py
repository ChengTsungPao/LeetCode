class MinStack:

    def __init__(self):
        self.stack = []
        self.sortstack = []

    def push(self, x: int) -> None:
        index = bisect.bisect_left(self.sortstack, x)
        self.sortstack.insert(index, x)
        self.stack.append(x)

    def pop(self) -> None:
        index = bisect.bisect_left(self.sortstack, self.stack[-1])
        del self.sortstack[index]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sortstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()