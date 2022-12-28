class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        @functools.lru_cache(None)
        def recur(x1, x2, y1):
            y2 = x1 + y1 - x2
            if max(x1, y1, x2, y2) >= n or min(grid[x1][y1], grid[x2][y2]) < 0:
                return -float("inf")
            elif x1 == x2 == y1 == y2 == n - 1:
                return (grid[x1][y1] == 1) * 1
            
            D1D2 = recur(x1 + 1, x2 + 1, y1 + 0)
            D1R2 = recur(x1 + 1, x2 + 0, y1 + 0)
            R1D2 = recur(x1 + 0, x2 + 1, y1 + 1)
            R1R2 = recur(x1 + 0, x2 + 0, y1 + 1)
            
            score = max(D1D2, D1R2, R1D2, R1R2)
            
            return score + grid[x1][y1] if x1 == x2 and y1 == y2 else score + grid[x1][y1] + grid[x2][y2]
        
        score = recur(0, 0, 0)
        return score if score != -float("inf") else 0