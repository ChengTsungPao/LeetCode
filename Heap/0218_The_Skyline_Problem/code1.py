class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        x_set = set()
        buildingDict = collections.defaultdict(list)
        for x1, x2, h in buildings:
            x_set |= {x1, x2}
            buildingDict[x1].append((x2, h))
        
        ans = []
        heap  = []
        for x in sorted(x_set):
            # remove end skyline
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            
            # add new skyline
            for x2, h in buildingDict[x]:
                heapq.heappush(heap, (-h, x2))
                
            h = -heap[0][0] if heap else 0
            if not ans or h != ans[-1][1]:
                ans.append([x, h])
            
        return ans
