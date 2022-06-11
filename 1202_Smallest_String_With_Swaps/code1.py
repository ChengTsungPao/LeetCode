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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        DS = disjoint_set()
        
        for index in range(n):
            DS.build(index)
            
        for index1, index2 in pairs:
            DS.union(index1, index2)
            
        groupsChs = collections.defaultdict(list)
        groupsIndices = collections.defaultdict(list)
        for index in range(n):
            p = DS.findParent(index)
            groupsChs[p].append(s[index])
            groupsIndices[p].append(index)
            
        ans = [""] * n
        for key in groupsChs.keys():
            for ch, index in zip(sorted(groupsChs[key]), groupsIndices[key]):
                ans[index] = ch
                
        return "".join(ans)