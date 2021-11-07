class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        '''        
        rabbbit
        11111111
        11111110  t
        11111100  it
        33321000  bit
        33310000  bbit
        33000000  abbit
        30000000  rabbit        
        '''
        
        dp = [[1 if i == 0 else 0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]

        for i in range(1, len(t) + 1):
            for j in range(len(s) - i, -1, -1):
                
                # 相等 => 目前相等的這個字母 搭配 前一層j + 1之後有幾種組合 + 這一層j + 1之後有幾種組合
                # 不等 => 這一層j + 1之後有幾種組合
                if s[j] == t[-i]:
                    dp[i][j] = dp[i][j + 1] + dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        
        return dp[-1][0]