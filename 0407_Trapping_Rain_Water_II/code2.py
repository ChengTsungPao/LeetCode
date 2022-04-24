class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m = len(heightMap)
        n = len(heightMap[0])
        
        heap = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        ans = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or (i_, j_) in visited:
                    continue
                    
                ans += max(h - heightMap[i_][j_], 0)
                heapq.heappush(heap, (max(heightMap[i_][j_], h), i_, j_))
                visited.add((i_, j_))
                        
        return ans