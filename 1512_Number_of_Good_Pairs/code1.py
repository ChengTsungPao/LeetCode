class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return sum([v * (v - 1) // 2 for u, v in count.items()])