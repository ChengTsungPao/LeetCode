class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = []
        self.setup(encoding)
        
        
    def setup(self, encoding):
        for i in range(len(encoding) - 1, -1, -2):
            if encoding[i - 1] == 0:
                continue
            self.encoding.append([encoding[i], encoding[i - 1]])
        
        
    def next(self, n: int) -> int:
        if len(self.encoding) == 0:
            return -1

        while self.encoding and n > 0: 
            value, count = self.encoding[-1]
            
            if n >= count:
                n -= count
                self.encoding.pop()
            else:
                self.encoding[-1][1] -= n
                n = 0
        
        return value if n == 0 else -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)