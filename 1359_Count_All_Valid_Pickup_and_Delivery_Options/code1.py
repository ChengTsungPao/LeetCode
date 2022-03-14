class Solution:
    def countOrders(self, n: int) -> int:
        
        # dp[n] = dp[n - 1] 插入兩個的數字 (除以2 => 有次序)
        
        dp = 1
        for i in range(1, n):
            dp = dp * (2 * i + 1) * (2 * i + 2) // 2
            
        return dp % (10 ** 9 + 7)