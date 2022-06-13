class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        dp = [0] + [float("inf")] * n
        
        for i in range(1, n + 1):
            for f in range(1, i + 1):
                dp[i] = min(dp[i], max(dp[i - f], f - 1) + 1)
        
        return dp[n]