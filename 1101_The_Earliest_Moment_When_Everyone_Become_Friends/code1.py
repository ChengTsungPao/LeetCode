class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.countRoot = 0
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.countRoot += 1
        
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
        self.countRoot -= 1
        
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        DS = disjoint_set()
        for node in range(n):
            DS.build(node)
            
        for time, node1, node2 in sorted(logs):
            DS.union(node1, node2)
            if DS.countRoot == 1:
                return time
            
        return -1