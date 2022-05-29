class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.zeroSample = set(list(range(m * n)))
        
    def flip(self) -> List[int]:
        index = random.sample(self.zeroSample, 1)[0]
        self.zeroSample.remove(index)
        return [index // self.n, index % self.n]

    def reset(self) -> None:
        self.zeroSample = set(list(range(self.m * self.n)))
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()