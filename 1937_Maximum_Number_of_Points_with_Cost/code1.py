class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m = len(points)
        n = len(points[0])
        
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + points[i][j] - abs(j - k))
                    
        return max(dp[m - 1])