class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        p = collections.Counter(p)
        stmp = collections.Counter(s[:length])
        ans = [0] * (stmp == p)
        for i in range(1, len(s) - length + 1):
            stmp[s[i - 1]] -= 1
            stmp[s[i + length - 1]] += 1
            if s[i - 1] not in p:
                p[s[i - 1]] = 0
            if s[i + length - 1] not in p:
                p[s[i + length - 1]] = 0
            if stmp == p:
                ans.append(i)
        return ans