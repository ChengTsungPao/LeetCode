class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        n = len(buildings)
        buildings.sort()
        
        xPosition = set()
        for x1, x2, _ in buildings:
            xPosition.add(x1)
            xPosition.add(x2)
        
        ans = []
        heap = []
        i = 0
        for x in sorted(xPosition):
            while i < n and buildings[i][0] <= x:
                x1, x2, h = buildings[i]
                heapq.heappush(heap, (-h, x2))
                i += 1
                
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            
            h = -heap[0][0] if heap else 0
            if not ans or h != ans[-1][1]:
                ans.append([x, h])
            
        return ans