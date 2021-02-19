class Solution:
    def fib(self, n: int) -> int:
        
        def F(n, memo = {}):
            if n not in memo:
                if n <= 1:
                    return n
                memo[n] =  F(n - 1, memo) + F(n - 2, memo)
            return memo[n]
            
        return F(n)