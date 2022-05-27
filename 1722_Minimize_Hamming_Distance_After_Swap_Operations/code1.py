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
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        DS = disjoint_set()
        
        for index in range(n):
            DS.build(index)
            
        for index1, index2 in allowedSwaps:
            DS.union(index1, index2)
            
        status = collections.defaultdict(list)
        for index in range(n):
            p = DS.findParent(index)
            status[p].append(index)
            
        def getDistance(indices):
            statusTarget = collections.defaultdict(int)
            for index in indices:
                statusTarget[target[index]] += 1
            count = 0
            for index in indices:
                sourceNum = source[index]
                if statusTarget[sourceNum] > 0:
                    statusTarget[sourceNum] -= 1
                else:
                    count += 1            
            return count
        
        ans = 0
        for indices in status.values():
            ans += getDistance(indices)
            
        return ans