class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.increase = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.maxSize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) <= 0:
            return -1
        lastIndex = len(self.stack) - 1
        addValue = self.increase[lastIndex]
        if lastIndex >= 1:
            self.increase[lastIndex - 1] += addValue
        self.increase[lastIndex] = 0
        return self.stack.pop() + addValue
        
    def increment(self, k: int, val: int) -> None:
        if len(self.stack) <= 0:
            return
        self.increase[min(k, len(self.stack)) - 1] += val
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)