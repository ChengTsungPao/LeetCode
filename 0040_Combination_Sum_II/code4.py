class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        
        dp = [[[] for j in range(target + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = [[]]
            
        for i in range(n - 1, -1, -1):
            for j in range(1, target + 1):
                for k in range(i, n):
                    if (k == i or candidates[k - 1] < candidates[k]) and j - candidates[k] >= 0:
                        for ret in dp[k + 1][j - candidates[k]]:
                            dp[i][j].append([candidates[k]] + ret)
                            
        return dp[0][target]