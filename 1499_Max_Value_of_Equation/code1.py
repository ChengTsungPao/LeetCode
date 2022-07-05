class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

        ans = -float("inf")
        heap = []

        for x, y in points:
            
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                ans = max(ans, -heap[0][0] + (y + x))

            heapq.heappush(heap, (-(y - x), x))
        
        return ans