class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
            
                if i >= n or j >= m:
                    return 0

                ans = 0
                if text1[i] == text2[j]:
                    ans = max(ans, recur(i + 1, j + 1) + 1)
                else:
                    ans = max(ans, recur(i + 1, j), recur(i, j + 1))
                    
                memo[i, j] = ans
                
            return memo[i, j]
        
        return recur(0, 0)