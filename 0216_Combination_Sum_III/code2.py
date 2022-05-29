class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(10 + 1)]
        
        for i in range(10, 0, -1):
            for j in range(n + 1):
                for m in range(k + 1):
                    if j == 0 and m == 0:
                        dp[i][j][m] = [[]]
                    elif m == 0 or i >= 10:
                        dp[i][j][m] = []
                    else:
                        ans = []
                        for p in range(i, 9 + 1):
                            if j - p >= 0:
                                for ret in dp[p + 1][j - p][m - 1]:
                                    ans.append([p] + ret)
                        dp[i][j][m] = ans
                        
        return dp[1][n][k]