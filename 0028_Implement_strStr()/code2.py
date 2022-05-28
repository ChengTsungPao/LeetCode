class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # KMP Algorithm
        # Step1 => Get Longest Prefix Substring
        # Step2 => Use Longest Prefix Substring to matching
        
        m = len(needle)
        n = len(haystack)
        
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
        
        LPS = getLPS(needle)
        
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = LPS[j - 1]
                
            if j == m:
                return i - m
            
        return -1