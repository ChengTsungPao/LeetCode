class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = {}
        def dfs(index):
            if index not in dp:
                if index == len(s):
                    return [[]]
                layer = []
                for i in range(index, len(s)):
                    temp = s[index:i + 1]
                    if temp == temp[::-1]:
                        for j in dfs(i + 1):
                            layer += [[temp] + j]
                dp[index] = layer
            return dp[index]
        return dfs(0)