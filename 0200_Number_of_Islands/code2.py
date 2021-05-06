class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):    
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == "0":
                return False
            
            grid[i][j] = "0"
            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            
            return True
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += dfs(i, j)
                    
        return ans