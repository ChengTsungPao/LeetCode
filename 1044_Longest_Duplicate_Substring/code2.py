class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        n = len(s)
        
        ans = ""
        index = 0
        length = 1
        
        while index + length < n:
            if s[index: index + length] in s[index + 1:]:
                ans = s[index: index + length]
                length += 1
            else:
                index += 1
                
        return ans