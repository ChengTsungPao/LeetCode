class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        n = len(a)
        
        def isPalindrome(i, j, s):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j
        
        def checkPalindrome(a, b):
            i = 0
            j = n - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return isPalindrome(i, j, a) or isPalindrome(i, j, b)
        
        return checkPalindrome(a, b) or checkPalindrome(b, a)