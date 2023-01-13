class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        words = set(words)
        
        def isConcatenatedWord(idx, word):
            if idx >= len(word):
                return True 
            
            ret = False 
            subWord = ""
            for i in range(idx, len(word) - (idx == 0)):
                subWord += word[i]
                ret = ret or (subWord in words and isConcatenatedWord(i + 1, word))
                
            return ret
                
        return [word for word in words if isConcatenatedWord(0, word)]
