class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        if startValue > target:
            return startValue - target
        
        dp = [0] * (target + 1)
        dp[startValue] = 0
        
        for i in range(startValue):
            dp[i] = startValue - i
        
        for i in range(startValue + 1, target + 1):
            if i % 2:
                dp[i] = dp[(i + 1) // 2] + 2
            else:
                dp[i] = min(dp[i // 2] + 1, dp[(i + 2) // 2] + 3)
                
        return dp[target]