class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # f(i) + g(j) = (prices[j] + dp[j + 2]) - (prices[i])
        
        n = len(prices)
        
        maxScore = 0
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], maxScore - prices[i])
            maxScore = max(maxScore, prices[i] + dp[i + 2])
                    
        return dp[0]