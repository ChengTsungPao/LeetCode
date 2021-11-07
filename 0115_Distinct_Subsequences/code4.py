class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # dp 只需參考上一層，因此參考完後可以pop掉
        
        n, m = len(s), len(t)
        dp = [[1] * (n + 1)]           
        
        for i in range(m):
            dp.insert(0, [0] * (n + 1))
            
            for j in range(n - i - 1, -1, -1):
                if s[j] == t[-i - 1]:
                    dp[0][j] = dp[0][j + 1] + dp[1][j + 1]
                else:
                    dp[0][j] = dp[0][j + 1]
                    
            dp.pop()
            
        return dp[0][0]