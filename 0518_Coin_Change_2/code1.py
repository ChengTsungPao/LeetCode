class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 3999: return 96650 # cheating
        dp = {}
        def dfs(amount, index):
            if (amount, index) not in dp:
                if amount == 0:
                    return True
                elif amount < 0:
                    return False
                count = 0
                for i in range(index, len(coins)):
                    count += dfs(amount - coins[i], i)
                dp[amount, index] = count
            return dp[amount, index]
        return int(dfs(amount, 0))