class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        memo = {}
        def recur(i, j, mulIndex):
            
            if (i, j) not in memo:
            
                if mulIndex >= len(multipliers):
                    return 0

                memo[i, j] = max(nums[i] * multipliers[mulIndex] + recur(i + 1, j, mulIndex + 1), \
                                 nums[j] * multipliers[mulIndex] + recur(i, j - 1, mulIndex + 1))

            return memo[i, j]
        
        return recur(0, len(nums) - 1, 0)