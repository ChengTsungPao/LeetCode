class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return ""
            
            grid[i][j] = 0
            
            ans = "{}_{}_".format(i - shiftX, j - shiftY)
            ans += dfs(i + 0, j + 1) + dfs(i + 1, j + 0)
            ans += dfs(i + 1, j + 0)
            ans += dfs(i - 1, j + 0)
            ans += dfs(i + 0, j - 1)
            
            return ans
            
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shiftX, shiftY = i, j
                    ans.add(dfs(i, j))
                    
        return len(ans)