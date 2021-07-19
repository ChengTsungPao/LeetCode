class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        # dp[i, j] => A[:i + 1] 和 B[:j + 1] 的 maxUncrossedLines
        
        dp = collections.defaultdict(int)
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i, j] = dp[i - 1, j - 1] + 1
                else:
                    dp[i, j] = max(dp[i, j - 1], dp[i - 1, j])
        
        return dp[len(A) - 1, len(B) - 1]
