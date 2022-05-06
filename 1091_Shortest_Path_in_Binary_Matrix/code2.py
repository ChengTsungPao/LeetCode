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
        
        def getScore(i, j):
            return max((m - 1) - i, (n - 1) - j)
        
        heap = [(1 * 2 + getScore(0, 0), 1, 0, 0)]
        
        while heap:
            score, step, i, j = heapq.heappop(heap)
            
            if i == m - 1 and j == n - 1:
                return step
            
            for di, dj in direction:
                i_, j_ = i + di, j + dj
                if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == 1:
                    continue
                
                grid[i_][j_] = 1
                newScore = getScore(i_, j_) + (step + 1) * 2
                heapq.heappush(heap, (newScore, step + 1, i_, j_))
                
        return -1