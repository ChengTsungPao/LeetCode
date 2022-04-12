class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
            
            
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                
                left = preSum[j + 1] - preSum[i + 1]
                right = preSum[j] - preSum[i]
                
                if i + 1 < n:
                    dp[i][j] = max(dp[i][j], left - dp[i + 1][j])  
                else:
                    dp[i][j] = max(dp[i][j], left) 
                    
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], right - dp[i][j - 1]) 
                else:
                    dp[i][j] = max(dp[i][j], right) 
                
        return dp[0][n - 1]