class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {0: False, 1: True}
        for i in range(2, n + 1):
            dp[i] = False
            for j in range(1, int(i ** 0.5) + 1):
                if dp[i - j ** 2] == False:
                    dp[i] = True
                    break
        return dp[n]