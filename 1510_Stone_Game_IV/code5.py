class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)
        
        for i in range(n + 1):
            if i == 0:
                dp[i] = False
            elif i == 1:
                dp[i] = True
            else:
                ans = False
                for j in range(1, int(i ** 0.5) + 1):
                    ans = ans or not dp[i - j ** 2]
                dp[i] = ans
                
        return dp[n]