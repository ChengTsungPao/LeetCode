class disjoin_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.group = 0
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.group += 1
        
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
        
        self.group -= 1
        
        if self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        elif self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.weight[p1] += 1
            
    def getGroupNum(self):
        return self.group

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        DS = disjoin_set()
        
        connectionsNum = len(connections)
        
        for node in range(n):
            DS.build(node)
        
        for node1, node2 in connections:
            if DS.findParent(node1) != DS.findParent(node2):
                DS.union(node1, node2)
                connectionsNum -= 1

        return DS.getGroupNum() - 1 if connectionsNum >= DS.getGroupNum() - 1 else -1