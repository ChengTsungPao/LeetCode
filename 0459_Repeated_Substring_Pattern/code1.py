class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        m = len(s)
        
        def getLPS(s):
            LPS = [0] * m
            i = 1
            preLPS = 0
            while i < m:
                if s[i] == s[preLPS]:
                    LPS[i] = preLPS + 1
                    preLPS += 1
                    i += 1
                elif preLPS == 0:
                    LPS[i] = 0
                    i += 1
                else:
                    preLPS = LPS[preLPS - 1]
            return LPS
        
        LPS = getLPS(s)
        lps = LPS[-1]
        return lps > 0 and m % (m - lps) == 0