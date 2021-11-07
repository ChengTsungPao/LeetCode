class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def recur(wordIndex, memo = set()):
            
            if wordIndex not in memo:
            
                if wordIndex == len(s):
                    return True

                for word in wordDict:
                    start, end = wordIndex, wordIndex + len(word)
                    if s[start : end] == word and recur(end):
                        return True
                    
                memo.add(wordIndex)
                
            return False
        
        return recur(0)