class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 1
        ans = ""
        def dfs(s):
            nonlocal ans
            nonlocal count
            if(len(s) == n):
                if(count == k):
                    ans = s
                    return True
                count += 1
                return
            for ch in ["a", "b", "c"]:
                if((len(s) == 0 or s[-1] != ch) and dfs(s + ch)):
                    return True
        dfs("")
        return ans
