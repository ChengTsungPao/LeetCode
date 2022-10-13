class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        val = grid[0][0]
        dp[0][0][val % k] = 1
        
        for i in range(1, m):
            val = grid[i][0]
            for v, c in enumerate(dp[i - 1][0]):
                s = (v + val) % k
                dp[i][0][s] += c % MOD
                
        for j in range(1, n):
            val = grid[0][j]
            for v, c in enumerate(dp[0][j - 1]):
                s = (v + val) % k
                dp[0][j][s] += c % MOD
                
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                for v, c in enumerate(dp[i][j - 1]):
                    s = (v + val) % k
                    dp[i][j][s] += c % MOD
        
                for v, c in enumerate(dp[i - 1][j]):
                    s = (v + val) % k
                    dp[i][j][s] += c % MOD  
                    
        return dp[-1][-1][0] % MOD