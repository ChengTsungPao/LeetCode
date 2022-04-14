class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
                
        n = len(wordsDict)
        ans = float("inf")
        
        same = word1 == word2
        word1Index, word2Index = float("inf"), -float("inf")
        
        for index in range(n):
            word = wordsDict[index]
            if word == word1:
                if same:
                    word1Index = word2Index
                    word2Index = index
                else:
                    word1Index = index
            elif word == word2:
                word2Index = index
            
            ans = min(ans, abs(word1Index - word2Index))

        return ans