class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]            
            
        dp = [0] * n
        dp[n - 2] = preSum[n] - dp[n - 1]
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], preSum[i + 2] - dp[i + 1])  
            
        return dp[0]