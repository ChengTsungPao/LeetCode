class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # 此程式為recur改為bottom up的dp形式
        # dp的意義為利用Insert、Delete、Replace走到(i, j)，最少還要花dp[i][j]才能走到終點
        
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
            
        for i in range(len(word2) + 1):
            dp[len(word1)][i] = len(word2) - i
            
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1]) + 1
        
        return dp[0][0]