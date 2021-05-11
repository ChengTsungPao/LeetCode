class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans, s = "", s.lstrip()
        
        for i in range(len(s)):
            if s[i].isalpha() or s[i] == "." or s[i] == " " or (len(ans) > 0 and (s[i] == "+" or s[i] == "-")):
                break
            if s[i].isdigit() or s[i] == "+" or s[i] == "-":
                ans += s[i]
         
        if ans == "" or ans == "+" or ans == "-":
            return 0

        ans = int(ans)
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        else:
            return ans
