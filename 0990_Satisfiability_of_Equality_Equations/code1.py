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
        if self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        DS = disjoint_set()
        
        for equation in equations:
            if "==" not in equation:
                continue
            
            node1, node2 = equation.split("==")
            DS.build(node1)
            DS.build(node2)
            DS.union(node1, node2)
            
        for equation in equations:
            if "!=" not in equation:
                continue            
            
            node1, node2 = equation.split("!=")  
            DS.build(node1)
            DS.build(node2)
            if DS.findParent(node1) == DS.findParent(node2):
                return False
            
        return True