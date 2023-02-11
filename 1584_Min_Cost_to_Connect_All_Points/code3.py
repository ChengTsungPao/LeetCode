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
            return
        
        if self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        def getManhattanDistance(pointi, pointj):
            return abs(pointi[0] - pointj[0]) + abs(pointi[1] - pointj[1])
        
        arr = []
        for i in range(n):
            for j in range(i + 1, n):
                arr.append((getManhattanDistance(points[i], points[j]), i, j))
        arr.sort()
        
        DS = disjoint_set()
        
        ans = edge = 0
        for score, i, j in arr:
            DS.build(i)
            DS.build(j)
            
            if DS.findParent(i) == DS.findParent(j):
                continue
                
            ans += score
            edge += 1
            DS.union(i, j)
            
            if edge == n - 1:
                break
            
        return ans