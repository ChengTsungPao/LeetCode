class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0, 1]
        for i in range(n):
            dp = [dp[1], dp[0] + dp[1]]
            
        return dp[0]