class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:  
        ans, row, col = 0, len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    ans += - (i + 1 < row and grid[i + 1][j]) - (i - 1 >= 0 and grid[i - 1][j]) \
                           - (j + 1 < col and grid[i][j + 1]) - (j - 1 >= 0 and grid[i][j - 1]) + 4
        return ans