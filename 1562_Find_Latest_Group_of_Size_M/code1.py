class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.root = {}
        self.count = collections.defaultdict(int)
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.root[node] = 1
            self.count[1] += 1
            
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        if node1 not in self.parent or node2 not in self.parent:
            return
        
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        
        if p1 == p2:
            return
        
        self.count[self.root[p1]] -= 1
        self.count[self.root[p2]] -= 1
        self.count[self.root[p1] + self.root[p2]] += 1
        
        if self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
            self.root[p2] += self.root[p1]
            del self.root[p1]
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.root[p1] += self.root[p2]
            del self.root[p2]
        else:
            self.parent[p2] = p1
            self.weight[p1] += 1
            self.root[p1] += self.root[p2]
            del self.root[p2]

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        DS = disjoint_set()
        
        n = len(arr)
        ans = -1
        
        for i, node in enumerate(arr):
            DS.build(node)
            
            DS.union(node, node - 1)
            DS.union(node, node + 1)
                
            if DS.count[m] > 0:
                ans = i + 1
                
        return ans