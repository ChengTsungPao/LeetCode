# 阿寶
class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.costs = {}
        
    def build(self, node, cost):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.costs[node] = cost
            
    def getCost(self, node):
        p = self.findParent(node)
        return self.costs[p]
            
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
            self.costs[p2] = min(self.costs[p1], self.costs[p2])
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.costs[p1] = min(self.costs[p1], self.costs[p2])
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
            self.costs[p2] = min(self.costs[p1], self.costs[p2])
            
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        # Kruskal's algorithm
        
        DS = disjoint_set()
        
        heap = []
        for node, nextNode, pathCost in pipes:
            heap.append((pathCost, node, nextNode))
            
        heapq.heapify(heap)
        
        ans = sum(wells)
        total_edge = n - 1
        
        while heap and total_edge < n:
            pathCost, node1, node2 = heapq.heappop(heap)
            DS.build(node1, wells[node1 - 1])
            DS.build(node2, wells[node2 - 1])
            wellCost = max(DS.getCost(node1), DS.getCost(node2))
            if wellCost > pathCost and DS.union(node1, node2):
                ans = ans - wellCost + pathCost
                total_edge -= 1
                
        return ans