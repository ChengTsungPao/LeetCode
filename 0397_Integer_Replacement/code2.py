class Solution:
    def integerReplacement(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            if i % 2:
                dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)
            else:
                dp[i] = dp[i // 2] + 1

        return dp[n]