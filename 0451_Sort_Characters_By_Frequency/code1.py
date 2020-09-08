class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(s)
        ans = ""
        for ch in sorted(s.items(), key=lambda x: x[1], reverse=True):
            ans += ch[0] * ch[1]
        return ans