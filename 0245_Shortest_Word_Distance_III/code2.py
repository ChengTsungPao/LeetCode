class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
                
        n = len(wordsDict)
        ans = float("inf")
        
        if word1 == word2:
            preIndex = float("inf")
            for index in range(n):
                word = wordsDict[index]
                if word == word1:
                    ans = min(ans, abs(index - preIndex))
                    preIndex = index
            return ans
            
        word1Index, word2Index = float("inf"), -float("inf")
        for index in range(n):
            word = wordsDict[index]
            if word == word1:
                word1Index = index
            if word == word2:
                word2Index = index
            
            ans = min(ans, abs(word1Index - word2Index))

        return ans