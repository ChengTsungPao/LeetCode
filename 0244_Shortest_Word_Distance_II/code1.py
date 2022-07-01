class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.index[word].append(i)
            
    def getDistance(self, word1, word2, memo = {}):
        if (word1, word2) in memo:
            return memo[word1, word2]
        
        n = len(self.index[word1])
        m = len(self.index[word2])
        
        minDistance = float("inf")
        i = j = 0
        while i < n and j < m:
            index1, index2 = self.index[word1][i], self.index[word2][j]
            
            minDistance = min(minDistance, abs(index1 - index2))
            if index1 < index2:
                i += 1
            else:
                j += 1
                
        memo[word1, word2] = memo[word2, word1] = minDistance
        return minDistance        

    def shortest(self, word1: str, word2: str) -> int:
        return self.getDistance(word1, word2)
        

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)