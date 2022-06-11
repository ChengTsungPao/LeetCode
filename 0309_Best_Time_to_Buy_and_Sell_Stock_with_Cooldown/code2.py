class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i + 1, n):
                dp[i] = max(dp[i], (prices[j] - prices[i]) + dp[j + 2])
                    
        return dp[0]