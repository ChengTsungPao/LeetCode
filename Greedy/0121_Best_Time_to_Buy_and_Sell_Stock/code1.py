class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        preMin = prices[0]
        
        for price in prices:
            ans = max(ans, price - preMin)
            preMin = min(preMin, price)
            
        return ans