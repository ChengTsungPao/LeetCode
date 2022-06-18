class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.rootCount = 0
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.rootCount += 1
            
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
        
        self.rootCount -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        ans = []
        DS = disjoint_set()
        
        for i, j in positions:
            DS.build((i, j))
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or (i_, j_) not in DS.parent:
                    continue
                DS.build((i_, j_))
                DS.union((i, j), (i_, j_))
            ans.append(DS.rootCount)
                
        return ans