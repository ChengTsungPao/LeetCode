class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = temp = s
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):     
                if temp == temp[::-1]:
                    return temp
                elif j != len(s) - i:
                    temp = temp[1:] + s[i + j]
            temp = start = start[:-1]
        return ""