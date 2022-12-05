class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        
        @functools.lru_cache(None)
        def recur(i, k, isbuy):
            if i >= n or k == 0:
                return 0
            
            if isbuy:
                return max(recur(i + 1, k, True), recur(i + 1, k - 1, False) + prices[i])
            else:
                return max(recur(i + 1, k, False), recur(i + 1, k, True) - prices[i])
            
        return recur(0, k, False)