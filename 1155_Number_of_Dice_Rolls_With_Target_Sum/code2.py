class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                for dice in range(1, k + 1):
                    if j - dice >= 0:
                        dp[i][j] += dp[i - 1][j - dice]
                        dp[i][j] %= MOD
                
        return dp[n][target]