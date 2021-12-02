class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        dp[i][j] => 到 (i, j) 至少所需之血量
        
        Init:
            dp[m][n] = -dungeon[m][n] + 1 if dungeon[m][n] <= 0 else 1
            
        Method:
            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = dp[i][j] if dp[i][j] > 0 else 1
        '''
        
        m, n = len(dungeon) - 1, len(dungeon[0]) - 1
        
        dungeon[m][n] = -dungeon[m][n] + 1 if dungeon[m][n] <= 0 else 1
        
        for i in range(m - 1, -1, -1):
            dungeon[i][n] = dungeon[i + 1][n] - dungeon[i][n]
            dungeon[i][n] = dungeon[i][n] if dungeon[i][n] > 0 else 1
            
        for j in range(n - 1, -1, -1):
            dungeon[m][j] = dungeon[m][j + 1] - dungeon[m][j]
            dungeon[m][j] = dungeon[m][j] if dungeon[m][j] > 0 else 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dungeon[i][j] = min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j]
                dungeon[i][j] = dungeon[i][j] if dungeon[i][j] > 0 else 1
                
        return dungeon[0][0]