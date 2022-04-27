class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def pick(self, target: int) -> int:
        index = 0
        count = 1
        for i in range(self.n):
            if self.nums[i] == target:
                if random.random() < 1 / count:
                    index = i
                count += 1
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)