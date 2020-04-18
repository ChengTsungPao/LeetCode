class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        index = [True, True]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if(obstacleGrid[i][j]):
                    obstacleGrid[i][j] = 0
                    if(i == 0):
                        index[0] = False
                    if(j == 0):
                        index[1] = False
                else:
                    if((i != 0 and j != 0) or (i == 0 and index[0]) or (j == 0 and index[1])):
                        obstacleGrid[i][j] = 1                            
                
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if(obstacleGrid[i][j] != 0):
                    obstacleGrid[i][j] =  obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]