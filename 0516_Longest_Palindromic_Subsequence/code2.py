class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
                
                if i > j:
                    return 0
                elif i == j:
                    return 1
                
                if s[i] == s[j]:
                    ret = recur(i + 1, j - 1) + 2
                else:
                    ret = max(recur(i + 1, j), recur(i, j - 1))
                    
                memo[i, j] = ret
                
            return memo[i, j]
        
        return recur(0, len(s) - 1)