class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = mat[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                
        for i in range(n):
            for j in range(m):
                row , col  = max(i - k + 0, 0), max(j - k + 0 , 0)
                row_, col_ = min(i + k + 1, n), min(j + k + 1 , m)
                mat[i][j] = dp[row_][col_] - dp[row][col_] - dp[row_][col] + dp[row][col]
                
        return mat