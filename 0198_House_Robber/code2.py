class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] => 當前能夠獲得的最大收益
        
        dp = [nums[0], max(nums[:2])]
        
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
                
        return dp[-1]