class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = reversed(s.split(" "))
        for word in s:
            if word != "":
                ans += " " + word
        return ans[1:]