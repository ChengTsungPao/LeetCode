class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = pow(10, 9) + 7
        ans = 0
        dp = [1] + [0] * high
        for i in range(1, high + 1):
            dp[i] += dp[i - zero] if i - zero >= 0 else 0
            dp[i] += dp[i - one]  if i - one  >= 0 else 0
            ans += dp[i] * (low <= i <= high)
            ans %= MOD
        return ans