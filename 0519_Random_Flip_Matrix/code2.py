class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.ones = set()
        
    def flip(self) -> List[int]:
        index = random.randrange(0, self.m * self.n)
        while index in self.ones:
            index = random.randrange(0, self.m * self.n)
        self.ones.add(index)
        return [index // self.n, index % self.n]

    def reset(self) -> None:
        self.ones = set()
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()