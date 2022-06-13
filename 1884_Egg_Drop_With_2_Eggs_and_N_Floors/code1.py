class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        memo = {}
        def recur(n):
            
            if n not in memo:
            
                if n <= 0:
                    return 0

                ans = float("inf")
                for f in range(1, n + 1):
                    ans = min(ans, max(recur(n - f), f - 1) + 1)
                    
                memo[n] = ans
            
            return memo[n]
        
        return recur(n)