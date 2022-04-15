class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # 參數說明: i => row, j => col, k => 該點往前追溯的所有可能
        # 計算數值: dp[i][j] => dp[i - 1][k] + points[i][j] - abs(j - k) 之 maximum
        
        # 分段討論 情況一: j >= k  =>  (dp[i - 1][k] + k) + (points[i][j] - j)  =>  f(k) + g(j), when i is constant
        # 分段討論 情況二: j <= k  =>  (dp[i - 1][k] - k) + (points[i][j] + j)  =>  f(k) + g(j), when i is constant
        
        # 由上述兩種情況可以知道 f(k) 和 g(j) 之最大值可以分開計算，因此複雜度可以從 O(m*n*n) 降成 O(m*n)
        
        m = len(points)
        n = len(points[0])
        
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        
        for i in range(1, m):
            
            # 計算 j >= k 的 f(k) 在 (i, j) 的最大值
            prefixMax = [0] * n
            prefixMax[0] = dp[i - 1][0] + 0
            for k in range(1, n):
                prefixMax[k] = max(prefixMax[k - 1], dp[i - 1][k] + k)
            
            # 計算 j <= k 的 f(k) 在 (i, j) 的最大值
            suffixMax = [0] * n                   
            suffixMax[n - 1] = dp[i - 1][n - 1] - (n - 1)
            for k in range(n - 2, -1, -1):
                suffixMax[k] = max(suffixMax[k + 1], dp[i - 1][k] - k)
            
            # 計算全段 f(k) + g(j) 最大值
            for j in range(n):
                dp[i][j] = max(prefixMax[j] + (points[i][j] - j), suffixMax[j] + (points[i][j] + j))     
                
        return max(dp[m - 1])