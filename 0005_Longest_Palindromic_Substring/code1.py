class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                temp = s[j : i + j]
                if temp == temp[::-1]:
                    return temp
        return ""