class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # 先拿後拿沒區別，所以遇到相等就拿
        # 遇到不相等就取remove、replace、insert
        
        def recur(i, j, memo = {}):
            
            if (i, j) not in memo:
                
                if i == len(word1) or j == len(word2):
                    return max(len(word1) - i, len(word2) - j)
                
                if word1[i] == word2[j]: 
                    memo[i, j] = recur(i + 1, j + 1, memo)
                else: 
                    memo[i, j] = min(recur(i + 1, j, memo), recur(i + 1, j + 1, memo), recur(i, j + 1, memo)) + 1
                    
            return memo[i, j]
        
        return recur(0, 0)