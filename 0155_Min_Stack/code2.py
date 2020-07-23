class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        if(self.minstack == [] or self.minstack[-1] >= x):
            self.minstack.append(x)
        self.stack.append(x)
        
    def pop(self) -> None:
        if(self.minstack[-1] == self.stack[-1]):              
            self.minstack.pop() 
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()