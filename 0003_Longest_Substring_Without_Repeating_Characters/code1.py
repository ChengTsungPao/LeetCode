class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j, status, ans = 0, 0, set(), 0
        
        while j < len(s):               
            
            while s[j] in status:
                status.remove(s[i])
                i += 1
            
            status.add(s[j])
            
            ans = max(ans, j - i + 1)
            
            j += 1
        
        return ans
