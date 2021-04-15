class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int: 
        
        m, n = len(dungeon), len(dungeon[0])
        
        for i in range(m - 1, -1, -1):
            
            for j in range(n - 1, -1, -1):
                
                value = dungeon[i][j]
                
                if i + 1 < m and j + 1 < n:
                    dungeon[i][j] = min(dungeon[i + 1][j], dungeon[i][j + 1])
                elif i + 1 < m:
                    dungeon[i][j] = dungeon[i + 1][j]
                elif j + 1 < n:
                    dungeon[i][j] = dungeon[i][j + 1]
                else:
                    dungeon[i][j] = 1
   
                dungeon[i][j] = max(dungeon[i][j] - value, 1)
                    
        return dungeon[0][0]