class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        n = len(s)
        
        for length in range(n - 1, 0, -1):
            dp = set()
            substr = s[:length]
            
            for i in range(length, n):
                dp.add(substr)
                substr = substr[1:] + s[i]
                
                if substr in dp:
                    return length
                
        return 0