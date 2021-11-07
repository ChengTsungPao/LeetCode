class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] => 選擇該位置的最大收益
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            for j in range(i - 1):
                dp[i] = max(dp[i], nums[i] + dp[j])
                
        return dp[0] if len(nums) == 1 else max(dp[-1], dp[-2])