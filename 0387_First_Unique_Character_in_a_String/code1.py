class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = collections.Counter(s)
        for i in range(len(s)):
            if(data[s[i]] == 1):
                return i
        return -1