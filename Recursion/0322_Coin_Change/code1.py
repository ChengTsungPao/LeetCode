class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        
        @functools.lru_cache(None)
        def recur(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float("inf")
            
            # choose coin
            ans = float("inf")
            for coin in coins:
                ans = min(ans, 1 + recur(amount - coin))
            return ans
        
        ans = recur(amount)
        return ans if ans != float("inf") else -1