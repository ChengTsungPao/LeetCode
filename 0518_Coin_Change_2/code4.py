class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (n + 1)
        
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                
                if i - coins[j - 1] >= 0:
                    dp[i][j] += dp[i - coins[j - 1]][j]
          
        return dp[amount][n]