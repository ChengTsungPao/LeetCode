class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        dp[i][j] => 到 (i, j) 的最小總合
        
        Init:
            dp[0][i] = sum(dp[0][0 ~ i])
            dp[j][0] = sum(dp[0 ~ j][0])
        
        Method:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][]j
        '''
        
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        return grid[-1][-1]