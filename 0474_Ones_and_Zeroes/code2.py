class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        dp[i][m][n] => 前i個 組成最多m個0和n個1 的最長subset
        
        Init:
            cost = number of 0 or 1
            score = number of your things
            
            dp[0][m][n] = 0
        
        Method:
            dp[i][m][n] = max(dp[i - 1][m][n], dp[i - 1][m - count_zero][n - count_one] + 1)
        '''
        
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
           
        for i in range(1, len(strs) + 1):
            count = collections.Counter(strs[i - 1])
            count_zero, count_one = count["0"], count["1"]
            
            for j in range(m + 1):
                for k in range(n + 1):
                    if j - count_zero >= 0 and k - count_one >= 0: 
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - count_zero][k - count_one] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[-1][-1][-1]