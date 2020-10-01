class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def result(s):
            ans = []
            for ch in s:
                if(ch == "#"):
                    if(ans != []):
                        ans.pop()
                else:
                    ans.append(ch)
            return ans
        if(result(S) == result(T)):
            return True
        else:
            return False