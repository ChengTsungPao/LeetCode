class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        direction = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                direction.append((di, dj))
        
        m = len(grid)
        n = len(grid[0])
        
        que = collections.deque([(0, 0, 1)])
        grid[0][0] = 1
        
        while que:
            i, j, step = que.pop()
            
            if i == m - 1 and j == n - 1:
                return step
            
            for di, dj in direction:
                i_, j_ = i + di, j + dj
                if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == 1:
                    continue
                    
                que.appendleft((i_, j_, step + 1))
                grid[i_][j_] = 1
                
        return -1