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
    def swimInWater(self, grid: List[List[int]]) -> int:
                
        n = len(grid)
        
        index = {}
        for i in range(n):
            for j in range(n):
                index[grid[i][j]] = (i, j)
                
        DS = disjoint_set()        
        for time in range(n ** 2):
            i, j = index[time]
            DS.build((i, j))
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i < n and 0 <= j < n) or (x, y) not in DS.parent:
                    continue
                DS.union((i, j), (x, y))
                
            if (0, 0) in DS.parent and (n - 1, n - 1) in DS.parent and DS.findParent((0, 0)) == DS.findParent((n - 1, n - 1)):
                return time
                
        return -1