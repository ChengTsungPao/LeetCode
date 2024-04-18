class UF:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.cost = {}
        
    def build(self, node, cost):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.cost[node] = cost
        
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2, cost):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        
        if p1 == p2:
            self.cost[p1] &= cost
            return
        
        if self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
            self.cost[p2] &= (self.cost[p1] & cost)
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.cost[p1] &= (self.cost[p2] & cost)
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
            self.cost[p2] &= (self.cost[p1] & cost)
            
    def getCost(self, node):
        p = self.findParent(node)
        return self.cost[p]
        
            
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF()
        
        for node1, node2, cost in edges:
            uf.build(node1, cost)
            uf.build(node2, cost)
            uf.union(node1, node2, cost)
            
        ans = []
        for node1, node2 in query:
            uf.build(node1, -1)
            uf.build(node2, -1)
            if uf.findParent(node1) != uf.findParent(node2):
                ans.append(-1)
            else:
                ans.append(uf.getCost(node1))
        
        return ans