class Solution:

    def __init__(self, w: List[int]):
        self.weight = [w[0]]
        for i in range(1, len(w)):
            self.weight += [self.weight[i - 1] + w[i]]
        
    def pickIndex(self) -> int:
        return bisect.bisect_right(self.weight, random.randint(0, self.weight[-1] - 1))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()