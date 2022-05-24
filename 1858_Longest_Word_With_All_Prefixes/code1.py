class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        lengthDict = collections.defaultdict(set)
        lengthDict[0].add("")
        for word in words:
            lengthDict[len(word)].add(word)
        
        ans = ""
        for length in range(1, max(lengthDict.keys()) + 1):
            
            for word in list(lengthDict[length]):
                if word[:-1] not in lengthDict[length - 1]:
                    lengthDict[length].remove(word)
                else:
                    ans = min(ans, word, key = lambda w: (-len(w), w))
            
            if not lengthDict[length]:
                break
                
        return ans