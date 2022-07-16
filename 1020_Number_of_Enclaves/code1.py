class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            
            dfs(i + 1, j + 0)
            dfs(i + 0, j + 1)
            dfs(i - 1, j + 0)
            dfs(i + 0, j - 1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
            
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
            
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans += grid[i][j]
                
        return ans