class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, _str, dp = {}):
            if (left, right) not in dp:
                if left > n or right > n or left < right:
                    return []
                elif left == n and right == n:
                    return [""]
                dp[left, right] = []
                for s in dfs(left + 1, right, _str + "(", dp):
                    dp[left, right] += ["(" + s]
                for s in dfs(left, right + 1, _str + ")", dp):
                    dp[left, right] += [")" + s]  
            return dp[left, right]
        return dfs(0, 0, "")