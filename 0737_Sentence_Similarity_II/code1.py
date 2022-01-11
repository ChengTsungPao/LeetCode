class disjoin_set():
    def __init__(self):
        self.parent = {}
        self.weight = {}
        
    def findParent(self, word):
        if self.parent[word] == word:
            return word
        self.parent[word] = self.findParent(self.parent[word])
        return self.parent[word]
    
    def Union(self, word1, word2):
        p1 = self.findParent(word1)
        p2 = self.findParent(word2)
        
        if p1 == p2:
            return
        
        if self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        elif self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        DIS = disjoin_set()
        
        for word1, word2 in similarPairs:
            if word1 not in DIS.weight:
                DIS.weight[word1] = 1
                DIS.parent[word1] = word1
            if word2 not in DIS.weight:
                DIS.weight[word2] = 1
                DIS.parent[word2] = word2
                
            DIS.Union(word1, word2)
  
        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            
            if word1 not in DIS.weight or word2 not in DIS.weight:
                return False
            
            p1 = DIS.findParent(word1)
            p2 = DIS.findParent(word2)
            
            if p1 != p2:
                return False
            
        return True
