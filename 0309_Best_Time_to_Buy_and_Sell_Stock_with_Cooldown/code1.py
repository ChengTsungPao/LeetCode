class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        memo = {}
        def recur(index):
            
            if index not in memo:
            
                if index >= n:
                    return 0

                ans = recur(index + 1)
                for nextIndex in range(index + 1, n):
                    if prices[nextIndex] - prices[index] > 0:
                        ans = max(ans, prices[nextIndex] - prices[index] + recur(nextIndex + 2))

                memo[index] = ans
                    
            return memo[index]
        
        return recur(0)