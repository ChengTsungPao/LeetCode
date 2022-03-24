class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        n = len(stoneValue)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stoneValue[i - 1]
            
        
        dp = [[0] * n for _ in range(n)]    
        
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    dp[i][j] = 0
                
                ans = 0
                for k in range(i, j):
                    left = preSum[k + 1] - preSum[i]
                    right = preSum[j + 1] - preSum[k + 1]

                    if left < right:
                        ans = max(ans, dp[i][k] + left)
                    elif left > right:
                        ans = max(ans, dp[k + 1][j] + right)
                    else:
                        ans = max(ans, dp[i][k] + left, dp[k + 1][j] + right)
                        
                dp[i][j] = ans
                
        return dp[0][n - 1]