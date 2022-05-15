class Solution:
    def numTilings(self, n: int) -> int:
        
        '''
        觀察各種結尾
        
        情況一 => dp[i - 1] * 1
        
        . x x o 
        . x x o 
        
        情況二 => dp[i - 2] * 1 <--- 只計算橫的避免重複
        
        . x o o
        . x o o 

        情況三 => dp[i - 3] * 2 + dp[i - 5] * 2 + dp[i - 7] * 2 ...
        
        . x o o           . x x o
        . x x o           . x o o
        
        情況四 => dp[i - 4] * 2 + dp[i - 6] * 2 + dp[i - 8] * 2 ...
        
        x     o           x x o o
        x x o o           x     o              
        '''
        
        MOD = 10 ** 9 + 7
        
        dp = [1] * max(n + 1, 4 + 1)
        dp[2] = 2
        dp[3] = 5
        dp[4] = 11
        
        for i in range(5, n + 1):
            
            dp[i] = dp[i - 1] + dp[i - 2]
            for j in range(i - 2):
                dp[i] += dp[j] * 2
                
            dp[i] %= MOD
            
        return dp[n]