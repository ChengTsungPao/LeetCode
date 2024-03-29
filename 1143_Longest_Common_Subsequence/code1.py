class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp[i][j] => text1[:i] 和 text2[:j] 的 longestCommonSubsequence
        # dp[i][j] 包含所有的 dp[a < i][b < j] 所以當 text1[i] != text2[j] => dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        return dp[-1][-1]