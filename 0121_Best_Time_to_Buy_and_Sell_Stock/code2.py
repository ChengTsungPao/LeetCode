class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_ = float("inf")
        for i in range(len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
            elif prices[i] - min_ > ans:
                ans = prices[i] - min_             
        return ans