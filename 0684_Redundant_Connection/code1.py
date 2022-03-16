class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 0
            
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        DS_Tree = disjoint_set()
        
        for node1, node2 in edges:
            
            DS_Tree.build(node1)
            DS_Tree.build(node2)
            
            if DS_Tree.union(node1, node2) == False:
                return [node1, node2]
        
        return []