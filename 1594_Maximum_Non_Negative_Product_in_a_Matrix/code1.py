class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [grid[0][0], grid[0][0]]
        
        for i in range(1, m):
            all_possible = [
                dp[i - 1][0][0] * grid[i][0],
                dp[i - 1][0][1] * grid[i][0]
            ]
            dp[i][0] = [min(all_possible), max(all_possible)]
            
        for j in range(1, n):
            all_possible = [
                dp[0][j - 1][0] * grid[0][j],
                dp[0][j - 1][1] * grid[0][j]
            ]
            dp[0][j] = [min(all_possible), max(all_possible)]
            
        for i in range(1, m):
            for j in range(1, n):
                all_possible = [
                    dp[i - 1][j][0] * grid[i][j],
                    dp[i - 1][j][1] * grid[i][j],
                    dp[i][j - 1][0] * grid[i][j],
                    dp[i][j - 1][1] * grid[i][j]
                ]
                dp[i][j] = [min(all_possible), max(all_possible)]
                
        return dp[m - 1][n - 1][1] % MOD if dp[m - 1][n - 1][1] >= 0 else -1