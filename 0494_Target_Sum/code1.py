class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def recur(index, target, memo = {}):
            
            if (index, target) not in memo:
            
                if len(nums) == index:
                    return (target == 0) * 1

                memo[index, target] = recur(index + 1, target - nums[index]) + recur(index + 1, target + nums[index])
            
            return memo[index, target]
        
        return recur(0, target)