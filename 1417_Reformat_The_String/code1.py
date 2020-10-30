class Solution:
    def reformat(self, s: str) -> str:
        n = []
        c = []
        for ch in s:
            if(ch.isdigit()):
                n.append(ch)
            else:
                c.append(ch)
        if(abs(len(n) - len(c)) > 1):
            return ""
        if(len(n) > len(c)):
            ans = ""
            for i in range(len(c)):
                ans += n[i] + c[i]
            ans += n[-1]
        else:
            ans = ""
            for i in range(len(n)):
                ans += c[i] + n[i] 
            if(len(n) != len(c)):
                ans += c[-1]
        return ans