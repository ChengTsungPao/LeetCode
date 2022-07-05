class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

        n = len(points)

        ans = -float("inf")
        heap = []

        for i in range(n):
            xi, yi = points[i]

            while heap and xi - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                ans = max(ans, -heap[0][0] + (yi + xi))

            heapq.heappush(heap, (-(yi - xi), xi))
        
        return ans