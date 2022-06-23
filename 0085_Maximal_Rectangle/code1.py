class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        ans = 0       
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # count number of left ones
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                    
                    # calculate rectangle area
                    width, height = float("inf"), 0
                    for k in range(i, -1, -1):
                        if matrix[k][j] == "1":
                            width, height = min(width, dp[k][j]), height + 1
                            ans = max(ans, width * height)
                        else:
                            break
                            
        return ans