class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [[0] * (i + 1) for i in range(100)]
        dp[0][0] = poured
        
        for i in range(99):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j + 0] += (dp[i][j] - 1) / 2
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
                
            if dp[i][(i + 1) // 2] <= 1:
                break

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1