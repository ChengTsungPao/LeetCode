class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(x, y):
            if (x, y) not in dp:
                if  x >= m or y >= n:
                    return 0
                elif x == m - 1 and y == n - 1:
                    return 1
                layer = 0
                layer += dfs(x + 1, y) + dfs(x, y + 1)
                dp[x, y] = layer
            return dp[x, y]        
        return dfs(0, 0)