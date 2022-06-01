class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        n = len(s)
        
        ans = 0
        index = 0
        length = 1
        
        while index + length < n:
            if s[index: index + length] in s[index + 1:]:
                ans = max(ans, length)
                length += 1
            else:
                index += 1
                
        return ans