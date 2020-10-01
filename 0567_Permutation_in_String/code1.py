class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        s1 = collections.Counter(s1)
        s2tmp = collections.Counter(s2[:length])
        if s2tmp == s1: return True
        for i in range(1, len(s2) - length + 1):
            s2tmp[s2[i - 1]] -= 1
            s2tmp[s2[i + length - 1]] += 1
            if s2[i - 1] not in s1:
                s1[s2[i - 1]] = 0
            if s2[i + length - 1] not in s1:
                s1[s2[i + length - 1]] = 0
            if s2tmp == s1:
                return True
        return False    