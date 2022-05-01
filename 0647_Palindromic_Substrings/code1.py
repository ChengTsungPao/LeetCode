class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        def countPalindromic(i, j):
            if j >= n:
                return 0
            
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
                
            return count
        
        ans = 0
        for i in range(n):
            ans += countPalindromic(i, i) + countPalindromic(i, i + 1)
            
        return ans