class Solution:
    def longestPrefix(self, s: str) -> str:
        
        # LPS => Longest Prefix Substring (KMP Algorithm)

        n = len(s)

        LPS = [0] * n
        i = 1
        preLPS = 0
        while i < n:
            if s[i] == s[preLPS]:
                LPS[i] = preLPS + 1
                preLPS += 1
                i += 1
            elif preLPS == 0:
                LPS[i] = 0
                i += 1
            else:
                preLPS = LPS[preLPS - 1]
        
        return s[:LPS[-1]]