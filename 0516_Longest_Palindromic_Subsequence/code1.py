class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[1] * len(s) for _ in range(len(s))]
        
        for i in range(len(s) - 1):
            i, j = i, i + 1
            if s[i] == s[j]:
                dp[i][j] = 2
        
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                i, j = i, i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]    
        