class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        @functools.lru_cache(None)
        def isValidStart(i, j):
            if i < 0 or j < 0 or grid[i][j] < 0:
                return False
            elif i == 0 and j == 0:
                return True
            return isValidStart(i - 1, j) or isValidStart(i, j - 1)
        
        @functools.lru_cache(None)
        def isValidEnd(i, j):
            if i >= n or j >= n or grid[i][j] < 0:
                return False
            elif i == n - 1 and j == n - 1:
                return True
            return isValidEnd(i + 1, j) or isValidEnd(i, j + 1)
        
        if not isValidEnd(0, 0):
            return 0
        
        valid_position = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and isValidStart(i, j) and isValidEnd(i, j):
                    valid_position.add((i, j))
        
        valid_position.add((0, 0))
        valid_position = sorted(valid_position)

        @functools.lru_cache(None)
        def recur(p1, p2, idx):
            if idx >= len(valid_position):
                return (grid[0][0] <= 0) * (-1)
            
            x , y  = valid_position[idx]
            x1, y1 = valid_position[p1]
            x2, y2 = valid_position[p2]
            
            ans = recur(p1, p2, idx + 1)
            if x >= x1 and y >= y1:
                _p1, _p2 = sorted([idx, p2])
                ans = max(ans, recur(_p1, _p2, idx + 1) + 1)
            if x >= x2 and y >= y2:
                _p1, _p2 = sorted([p1, idx])
                ans = max(ans, recur(_p1, _p2, idx + 1) + 1)
                
            return ans
        
        return recur(0, 0, 0)