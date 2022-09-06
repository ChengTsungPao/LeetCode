class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 概念: 反過來想，就是其中一個減一
        return sum(nums) - len(nums) * min(nums)