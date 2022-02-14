class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        分支 => ccab...abcc
        '''
        
        def isPalindrome(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break      

        return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)