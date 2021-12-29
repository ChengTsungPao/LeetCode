class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isSubsequence(word, memo = {}):
            
            if word not in memo:
                
                i = j = 0
                while i < len(s) and j < len(word):
                    if s[i] == word[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1

                memo[word] = j == len(word)
            
            return memo[word]
                
            
        count = 0
        for word in words:
            if isSubsequence(word):
                count += 1
                
        return count
        