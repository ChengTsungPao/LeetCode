class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        record = {}
        
        i = j = 0
        while j < len(s):
            
            if s[j] in record and record[s[j]] >= i:
                i = record[s[j]] + 1
            record[s[j]] = j
            
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans