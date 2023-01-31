class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        cache = {}
        que = collections.deque([((0, 0), k, 0)])
        
        while que:
            (x, y), k, step = que.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return step
            
            for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if not (0 <= x_ < m and 0 <= y_ < n):
                    continue
                    
                if (x_, y_) in cache and cache[x_, y_] >= k:
                    continue
                
                k_ = k - grid[x_][y_]
                if k < 0:
                    continue
                    
                cache[x_, y_] = k_
                que.append(((x_, y_), k_, step + 1))
                
        return -1