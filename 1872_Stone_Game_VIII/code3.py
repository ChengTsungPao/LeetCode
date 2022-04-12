class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
            
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            
            ans = -float("inf")
            for j in range(i + 1, n):
                ans = max(ans, preSum[j + 1] - dp[j])
                
            dp[i] = ans if ans != -float("inf") else 0   
            
        return dp[0]