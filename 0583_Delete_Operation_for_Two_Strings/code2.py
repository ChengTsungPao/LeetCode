class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)
        
        memo = {}
        def recur(i, j):
            if (i, j) not in memo:
            
                if i == m and j == n:
                    return 0
                elif i == m or j == n:
                    return max(m - i, n - j)
                
                if word1[i] == word2[j]:
                    distance = recur(i + 1, j + 1)
                else:
                    distance = min(recur(i, j + 1), recur(i + 1, j)) + 1
                    
                memo[i, j] = distance
                
            return memo[i, j]
        
        return recur(0, 0)