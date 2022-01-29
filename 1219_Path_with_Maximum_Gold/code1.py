class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == 0:
                return 0
            
            value = grid[i][j]
            grid[i][j] = 0
            
            ret = max(dfs(i + 1, j), dfs(i, j + 1), dfs(i - 1, j), dfs(i, j - 1)) + value
            
            grid[i][j] = value
            
            return ret
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, dfs(i, j))
                
        return ans