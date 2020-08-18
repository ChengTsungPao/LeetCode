class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def dfs(i, j):
            if (i, j) not in dp:
                if len(triangle) == i:
                    return 0
                dp[i, j] = min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
            return dp[i, j]
        return dfs(0, 0)