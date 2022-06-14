class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.children = set()
        
    def build(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.weight[node] = 1
            self.children.add(node)
    
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
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        DS = disjoint_set()
        
        text = text.split(" ")
        for word in text:
            DS.build(word)
        
        for word1, word2 in synonyms:
            DS.build(word1)
            DS.build(word2)
            DS.union(word1, word2)
            
        group = collections.defaultdict(list)
        for word in DS.children:
            p = DS.findParent(word)
            group[p].append(word)
        
        n = len(text)
        
        def recur(index):
            if index >= n:
                return [""]
            
            ans = []
            for changeWord in group[DS.findParent(text[index])]:
                for ret in recur(index + 1):
                    ans.append(changeWord + " " * (index < n - 1) + ret)
                        
            return ans
        
        return sorted(recur(0))