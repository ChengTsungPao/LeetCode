class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        '''
        不論正負，從(0, 0)出發的步數都一樣 (如果今天題目不是從(0, 0)出發，可以將整個坐標系平移到(0, 0))
        
        x + y = 0 => (0, 0) => 0
        x + y = 1 => (0, 1), (1, 0) => 3
        x + y = 2 => (1, 1), (0, 2), (2, 0) => 2
        '''
        
        def dfs(x, y, memo = {}):
            
            if (x, y) not in memo:
                
                if x + y == 0:
                    return 0
                elif x + y == 1:
                    return 3
                elif x + y == 2:
                    return 2
                
                memo[x, y] = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

            return memo[x, y]
        
        return dfs(abs(x), abs(y))
