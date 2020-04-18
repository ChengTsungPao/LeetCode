class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i != 0 and j != 0):
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                else:
                    grid[i][j] += max((i != 0) * grid[i-1][j], (j != 0) * grid[i][j-1])
        return grid[-1][-1]