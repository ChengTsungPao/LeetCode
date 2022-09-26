class Solution:
    def longestContinuousSubstring(self, s: str) -> int:        
        n = len(s)

        ans = 1
        i = 0
        for j in range(1, n):
            if ord(s[j]) - ord(s[j - 1]) != 1:
                i = j
            ans = max(ans, j - i + 1)
            
        return ans