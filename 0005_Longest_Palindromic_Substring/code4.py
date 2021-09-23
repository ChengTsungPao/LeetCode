class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def maxPalindrome(i, j):

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1, s[i + 1: j]       
            
        ans = ""
        maxLength = 0
        
        for i in range(len(s)):
            
            length, word = maxPalindrome(i, i)
            if maxLength < length:
                ans = word
                maxLength = length
                
            length, word = maxPalindrome(i, i + 1)
            if maxLength < length:
                ans = word
                maxLength = length
            
        return ans
