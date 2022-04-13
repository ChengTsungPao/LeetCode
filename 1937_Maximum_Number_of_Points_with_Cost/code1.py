class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        dp = [points[0].copy()]
        m, n = len(points), len(points[0])
        
        for i in range(1, m):
            
            dp.append([])
            for j in range(n):
                
                dp[i].append(0)
                for k in range(max(0, j - points[i][j]), min(n, j + points[i][j] + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + points[i][j] - abs(j - k))

        return max(dp[-1])