class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return False
            
            if grid[i][j] == 1:
                return True
            
            grid[i][j] = 1
            
            ret = True
            ret = dfs(i + 1, j + 0) and ret
            ret = dfs(i + 0, j + 1) and ret
            ret = dfs(i - 1, j + 0) and ret
            ret = dfs(i + 0, j - 1) and ret
            
            return ret
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += dfs(i, j)
                    
        return ans