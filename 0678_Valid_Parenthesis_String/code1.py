class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(index, stack):
            if((index, stack) not in dp):
                if(len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")"):
                    stack = stack[:-2]
                if(index == len(s)):
                    return stack == "" or set(stack) == set("*")
                if(s[index] == "*"):
                    ans = dfs(index + 1, stack) or dfs(index + 1, stack + "(") or dfs(index + 1, stack + ")")
                else:
                    ans = dfs(index + 1, stack + s[index])
                dp[index, stack] = ans
            return dp[index, stack]
        if(dfs(0, "")):
            return True
        else:
            return False