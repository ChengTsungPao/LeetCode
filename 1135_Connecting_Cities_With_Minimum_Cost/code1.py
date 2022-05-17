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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        # Kruskal's algorithm
        
        DS = disjoint_set()
        
        heap = []
        for node, nextNode, cost in connections:
            heap.append((cost, node, nextNode))
            
        heapq.heapify(heap)
        
        ans = 0
        total_edge = n - 1
        while heap and total_edge > 0:
            cost, node1, node2 = heapq.heappop(heap)
            DS.build(node1)
            DS.build(node2)
            if DS.union(node1, node2):
                ans += cost
                total_edge -= 1
                
        return ans if total_edge == 0 else -1