class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[i][amount] = 前i個 總合為amount的最小組合
        
        Init:
            cost = coins
            score = amount
        
            dp[0][amount] = float("inf")
            dp[i][0] = 1
        
        Method:
            dp[i][amount] = max(dp[i - 1][amount], dp[i][amount_ - coins[i]] + 1)
        '''
        
        dp = [[float("inf")] * (amount + 1) for _ in range(len(coins) + 1)]
        
        for i in range(len(coins) + 1):
            dp[i][0] = 0
        
        for i in range(1, len(coins) + 1):
            for amount_ in range(1, amount + 1):
                if amount_ - coins[i - 1] >= 0:
                    dp[i][amount_] = min(dp[i - 1][amount_], dp[i][amount_ - coins[i - 1]] + 1)
                else:
                    dp[i][amount_] = dp[i - 1][amount_]
           
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1
        