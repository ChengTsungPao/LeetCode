class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for ch in t:
            if index == len(s):
                return True
            index += s[index] == ch
        return index == len(s)