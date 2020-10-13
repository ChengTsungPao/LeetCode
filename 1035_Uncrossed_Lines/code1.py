class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = {}
        def dfs(i, j, count):
            if (i, j) not in dp:
                if i == len(A) or j == len(B):
                    return count
                if A[i] == B[j]:
                    dp[i, j] = dfs(i + 1, j + 1, count + 1) - count
                else:
                    dp[i, j] = max(dfs(i + 1, j + 0, count), dfs(i + 0, j + 1, count)) - count
            return count + dp[i, j]
        return dfs(0, 0, 0)