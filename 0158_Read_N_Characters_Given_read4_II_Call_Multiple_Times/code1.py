# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = collections.deque()
        
    def read(self, buf: List[str], n: int) -> int:
        while buf:
            buf.pop()
            
        while len(self.buffer) < n:
            buf4 = [""] * 4
            times = read4(buf4)
            if times == 0:
                break
            for i in range(times):
                self.buffer.append(buf4[i])
            
        for i in range(n):
            s = self.buffer.popleft() if self.buffer else ""
            buf.append(s)
            
        return n