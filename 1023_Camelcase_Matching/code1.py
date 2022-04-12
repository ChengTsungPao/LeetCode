class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def isMatch(word):
            n = len(word)
            m = len(pattern)
            
            i = j = 0
            while i < n:
                if j < m and word[i] == pattern[j]:
                    i += 1
                    j += 1
                elif ord(word[i]) >= 97:
                    i += 1
                else:
                    return False
                
            return j >= m
        
        
        ans = []
        for word in queries:
            ans.append(isMatch(word))
            
        return ans