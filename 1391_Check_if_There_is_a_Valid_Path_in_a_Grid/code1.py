class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        
        direction = [
            {None: None},
            {"L": "L", "R": "R"},
            {"U": "U", "D": "D"},
            {"R": "D", "U": "L"},
            {"L": "D", "U": "R"},
            {"R": "U", "D": "L"},
            {"L": "U", "D": "R"},
        ]
        
        move = {
            "L": ( 0, -1),
            "R": ( 0,  1),
            "D": ( 1,  0),
            "U": (-1,  0)
        }
        
        def nextPosition(i, j, d):
            nextD = direction[grid[i][j]][d]
            di, dj = move[nextD]
            grid[i][j] *= -1
            i, j = i + di, j + dj
            if not (0 <= i < m and 0 <= j < n) or nextD not in direction[grid[i][j]] or grid[i][j] < 0:
                return -1, -1, -1
            return i, j, nextD
        
        def simulation(i, j, d):
            grid[0][0] = abs(grid[0][0])
            i = j = 0
            while 0 <= i < m and 0 <= j < n:
                i, j, d = nextPosition(i, j, d)
                if i == m - 1 and j == n - 1:
                    return True
            return False
        
        d1, d2 = direction[grid[0][0]].keys()
        
        return (m == 1 and n == 1) or simulation(0, 0, d1) or simulation(0, 0, d2)