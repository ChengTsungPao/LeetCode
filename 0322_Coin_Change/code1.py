class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        dp = {}
        def dfs(amount):
            if amount not in dp:
                if amount == 0:
                    return 0
                elif amount < 0:
                    return float("inf")
                layer = float("inf")
                for c in coins:
                    layer = min(layer, dfs(amount - c) + 1)
                dp[amount] = layer
            return dp[amount]
        ans = dfs(amount)
        if ans == float("inf"):
            return -1
        else:
            return ans 