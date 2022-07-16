class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.count = {}
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.count[node] = 1
            
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
            self.count[p2] += self.count[p1]
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.count[p1] += self.count[p2]
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
            self.count[p2] += self.count[p1]

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        DS = disjoint_set()
        
        DS.build((-1, -1))
        for i in range(m):
            if grid[i][0] == 1:
                DS.build((i, 0))
                DS.union((-1, -1), (i, 0))
            if grid[i][n - 1] == 1:
                DS.build((i, n - 1))
                DS.union((-1, -1), (i, n - 1))
                
        for j in range(n):
            if grid[0][j] == 1:
                DS.build((0, j))
                DS.union((-1, -1), (0, j))
            if grid[m - 1][j] == 1:
                DS.build((m - 1, j))
                DS.union((-1, -1), (m - 1, j))                
        
        totalCount = 0
        for i in range(m):
            for j in range(n):
                totalCount += grid[i][j]
                
                if grid[i][j] == 1:
                    DS.build((i, j))
                    for x, y in [(i + 1, j), (i, j + 1)]:
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:
                            continue
                            
                        DS.build((x, y))
                        DS.union((i, j), (x, y))
                        
        p = DS.findParent((-1, -1))
        return totalCount - DS.count[p] + 1