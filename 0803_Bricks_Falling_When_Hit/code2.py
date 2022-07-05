class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.countChildren = {}
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.countChildren[node] = 1
    
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
            self.countChildren[p2] += self.countChildren[p1]
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.countChildren[p1] += self.countChildren[p2]
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
            self.countChildren[p2] += self.countChildren[p1]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        length = len(hits)
        
        DS = disjoint_set()
        
        ans = [0] * length
        for i, (x, y) in enumerate(hits):
            if grid[x][y] == 0:
                ans[i] = -1
            else:
                grid[x][y] = 0
                
        DS.build((-1, 0))  
        for y in range(1, n):
            DS.build((-1, y))
            DS.union((-1, y), (-1, y - 1))

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    DS.build((x, y))
                    for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                        if not (-1 <= x_ < m and 0 <= y_ < n) or (x_ >= 0 and grid[x_][y_] == 0):
                            continue
                        DS.build((x_, y_))
                        DS.union((x, y), (x_, y_))

        for i in range(length - 1, -1, -1):
            if ans[i] < 0:
                ans[i] = 0
                continue
            
            p = DS.findParent((-1, 0))
            preStableBricks = DS.countChildren[p]
            
            x, y = hits[i]
            grid[x][y] = 1
            DS.build((x, y))
            for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if not (-1 <= x_ < m and 0 <= y_ < n) or (x_ >= 0 and grid[x_][y_] == 0):
                    continue
                DS.build((x_, y_))
                DS.union((x, y), (x_, y_))
            
            p = DS.findParent((-1, 0))
            newStableBricks = DS.countChildren[p]
            
            ans[i] = 0 if newStableBricks == preStableBricks else newStableBricks - preStableBricks - 1
            
        return ans