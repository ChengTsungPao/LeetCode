class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        
        ans = 0
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if mat[i][0] == 1:
                dp[i][0] = 1
                
                minWidth = float("inf")
                for k in range(i, -1, -1):
                    minWidth = min(minWidth, dp[k][0])
                    ans += minWidth
        
        for i in range(n):
            for j in range(1, m):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                    
                    minWidth = float("inf")
                    for k in range(i, -1, -1):
                        minWidth = min(minWidth, dp[k][j])
                        ans += minWidth
                        
        return ans