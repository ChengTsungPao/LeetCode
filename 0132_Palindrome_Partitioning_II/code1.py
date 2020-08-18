class Solution:
    def minCut(self, s: str) -> int:
        dp = {}
        def dfs(index):
            if index not in dp:
                if index == len(s):
                    return -1
                layer = dfs(index + 1) + 1
                for i in range(index + 1, len(s)):
                    temp = s[index:i + 1]
                    if temp == temp[::-1]:
                        layer = min(layer, dfs(i + 1) + 1)
                dp[index] = layer
            return dp[index]
        return dfs(0)    