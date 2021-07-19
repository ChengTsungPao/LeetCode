class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        # dp[i][j] => A[:i] & B[:j] 的 maxUncrossedLines
        
        dp = [[0 for _ in range(len(B) + 1)]]
        
        for i in range(1, len(A) + 1):
            dp.append([0])
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i].append(dp[i - 1][j - 1] + 1)
                else:
                    dp[i].append(max(dp[i][j - 1], dp[i - 1][j]))
        
        return dp[len(A)][len(B)]
