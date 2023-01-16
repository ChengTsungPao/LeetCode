class Solution:
    def minInsertions(self, s: str) -> int:
        
        memo = {}
        def recur(i, j):
            
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    break
            
            if (i, j) not in memo:
                
                if i >= j:
                    return 0
                
                memo[i, j] = 1 + min(recur(i + 1, j), recur(i, j - 1))
                
            return memo[i, j]
        
        return recur(0, len(s) - 1)