class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp1 = [0] * n
        profitMax = 0
        curMin = prices[0]
        for i, price in enumerate(prices):
            profitMax = max(profitMax, price - curMin)
            dp1[i] = profitMax
            curMin = min(curMin, price)
            
        dp2 = [0] * n
        profitMax = 0
        curMax = dp1[0] - prices[0]
        for i, profit in enumerate(dp1):
            profitMax = max(profitMax, prices[i] + curMax)
            dp2[i] = profitMax
            curMax = max(curMax, profit - prices[i])

        return max(dp2)