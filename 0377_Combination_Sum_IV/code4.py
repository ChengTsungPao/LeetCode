class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        
        for i in range(target + 1):
            if i == 0:
                dp[i] = 1
            else:
                ret = 0
                for num in nums:
                    if i - num >= 0:
                        ret += dp[i - num]
                dp[i] = ret
                
        return dp[target]