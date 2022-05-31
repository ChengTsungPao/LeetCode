class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        minScore = float("inf")
        heap = [(-grid[0][0], 0, 0)]
        visited = set()
        
        while heap:
            score, i, j = heapq.heappop(heap)
            score *= -1
            
            if (i, j) in visited:
                continue
            
            minScore = min(minScore, score)
            if i == m - 1 and j == n - 1:
                return minScore
            
            visited.add((i, j))
            
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or (i_, j_) in visited:
                    continue
                
                heapq.heappush(heap, (-grid[i_][j_], i_, j_))
                
        return -1