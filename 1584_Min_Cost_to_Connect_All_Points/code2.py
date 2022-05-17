class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Prim's algorithm
        
        n = len(points)
        
        def getDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        randomIndex = random.randrange(0, n)
        point = tuple(points[randomIndex])
        heap = [(0, point)]
        
        ans = 0
        visited = set()
        
        while heap and len(visited) < n:
            cost, point = heapq.heappop(heap)
            
            if point in visited:
                continue
            ans += cost
            visited.add(point)
            
            for nextPoint in points:
                nextPoint = tuple(nextPoint)
                if nextPoint in visited:
                    continue
                heapq.heappush(heap, (getDistance(point, nextPoint), nextPoint))
                
        return ans if len(visited) == n else -1