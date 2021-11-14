class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # dp[i][j] => word1[:i] 和 word2[:j] 的 最大相同字母數目
        # dp[i][j] 包含所有的 dp[a < i][b < j] 所以當 word1[i] != word2[j] => dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        return len(word1) + len(word2) - 2 * dp[-1][-1]