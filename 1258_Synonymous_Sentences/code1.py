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
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        # 建立word之間的關係
        DS = disjoint_set()
        for word1, word2 in synonyms:
            DS.build(word1)
            DS.build(word2)
            DS.union(word1, word2)
        
        # 相同word放進同一個list
        wordDict = collections.defaultdict(list)
        for word in DS.parent.keys():
            wordDict[DS.findParent(word)].append(word)
        
        # 找出所有相同的text
        text = text.split(" ")
        def recur(index):
            if index >= len(text):
                return [""]
            
            ans = []
            if text[index] not in DS.parent:
                for ret in recur(index + 1):
                    if ret == "":
                        ans.append(text[index])
                    else:
                        ans.append(text[index] + " " + ret)
            else:
                for changeWord in wordDict[DS.findParent(text[index])]:
                    for ret in recur(index + 1):
                        if ret == "":
                            ans.append(changeWord)
                        else:
                            ans.append(changeWord + " " + ret) 
            return ans
        
        return sorted(recur(0))