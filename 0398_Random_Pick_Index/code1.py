class Solution:

    def __init__(self, nums: List[int]):
        self.index = collections.defaultdict(list)
        self.build(nums)
        
    def build(self, nums):
        for i in range(len(nums)):
            self.index[nums[i]].append(i)

    def pick(self, target: int) -> int:
        n = len(self.index[target])
        return self.index[target][random.randrange(0, n)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)