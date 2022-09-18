class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)
        
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = (word1[0] != word2[0]) * 2
        
        for i in range(1, m):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1

        for j in range(1, n):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j - 1] + 1
                
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[m - 1][n - 1]