class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

        ans = -float("inf")
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for x in range(i):
                    for y in range(j):
                        _sum = dp[i][j] - dp[x][j] - dp[i][y] + dp[x][y]
                        if _sum <= k: ans = max(ans, _sum)                        
                        
        return ans