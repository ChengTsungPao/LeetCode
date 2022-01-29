class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        actions =  [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        m = len(grid)
        n = len(grid[0])
        
        ans = float("inf")
        heap = [(0, 0, 0, 1)]
        found = {(0, 0): 0}

        while heap:
            score, x, y, count = heapq.heappop(heap)

            if x == m - 1 and y == n - 1:
                ans = min(ans, score)
                continue
            
            for dx, dy in actions:

                x_, y_ = x + dx, y + dy
                if not (0 <= x_ < m and 0 <= y_ < n):
                    continue
                
                newScore = score
                if actions[grid[x][y] - 1] != (dx, dy):
                    newScore += 1
                    
                if newScore >= found.get((x_, y_), float("inf")):
                    continue
                    
                found[x_, y_] = newScore
                heapq.heappush(heap, (newScore, x_, y_, count + 1))

        return ans