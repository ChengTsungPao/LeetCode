class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        
        if p1 == p2:
            return False
        
        if self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Kruskal’s algorithm
        
        n = len(points)
        
        def getDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                heap.append((getDistance(points[i], points[j]), tuple(points[i]), tuple(points[j])))
        
        DS = disjoint_set()
        heapq.heapify(heap)
        
        ans = 0
        total_edge = n - 1
        
        while heap and total_edge > 0:
            distance, point1, point2 = heapq.heappop(heap)
            DS.build(point1)
            DS.build(point2)
            if DS.union(point1, point2):
                ans += distance
                total_edge -= 1
                
        return ans if total_edge == 0 else -1