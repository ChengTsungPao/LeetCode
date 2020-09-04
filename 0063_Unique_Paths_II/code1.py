class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        def dfs(x, y):
            if (x, y) not in dp:
                if x >= len(obstacleGrid) or y >= len(obstacleGrid[0]) or obstacleGrid[x][y] == 1:
                    return 0
                elif x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
                    return 1
                layer = 0
                layer += dfs(x + 1, y) + dfs(x, y + 1)
                dp[x, y] = layer
            return dp[x, y]        
        return dfs(0, 0)
