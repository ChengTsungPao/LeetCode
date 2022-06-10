class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        dp = [[[[]]] + [[] for _ in range(k)] for _ in range(n + 2)]
        
        for i in range(n, 0, -1):
            for j in range(1, k + 1):
                for m in range(i, n - j + 2):
                    for ret in dp[m + 1][j - 1]:
                        dp[i][j].append([m] + ret)
                        
        return dp[1][k]