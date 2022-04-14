# 阿寶
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        indexArr = {word1: [], word2: []}
        for index in range(len(wordsDict)):
            if wordsDict[index] in indexArr:
                indexArr[wordsDict[index]].append(index)
                
        m = len(indexArr[word1])
        n = len(indexArr[word2])
                
        if word1 == word2:
            ans = float("inf")
            for i in range(1, m):
                word1Index, word2Index = indexArr[word1][i - 1], indexArr[word2][i]
                ans = min(ans, abs(word1Index - word2Index))
            return ans

        ans = float("inf")
        i = j = 0
        while i < m and j < n:
            word1Index, word2Index = indexArr[word1][i], indexArr[word2][j]
            ans = min(ans, abs(word1Index - word2Index))
            
            if word1Index < word2Index:
                i += 1
            elif word1Index > word2Index:
                j += 1
            else:
                break
                
        return ans