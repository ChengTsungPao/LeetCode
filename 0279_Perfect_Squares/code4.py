class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        for i in range(n + 1):
            for j in range(int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                    
        return dp[n]