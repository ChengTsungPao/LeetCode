class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        # dp[i][j][k] => 在位置 (i, j) 往 "上面"、"左邊"、"左上" 和 "右上" (分別對應 k = 0 ~ 3) 的最長連續1
        
        m = len(mat)
        n = len(mat[0])
        
        ans = 0
        dp = [[[0] * 4 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    for k, (i_, j_) in enumerate([(i-1, j), (i, j-1), (i-1, j-1), (i-1, j+1)]):
                        if 0 <= i_ < m and 0 <= j_ < n:
                            dp[i][j][k] = dp[i_][j_][k] + 1
                        else:
                            dp[i][j][k] = 1
                        ans = max(ans, dp[i][j][k])
                        
        return ans