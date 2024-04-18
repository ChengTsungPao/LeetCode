class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        for ch in s:
            cost = min(ord(ch) - ord("a"), ord("a") - ord(ch) + 26)
            if k >= cost:
                ans += "a"
            else:
                ans += chr(ord(ch) - k)
            k = max(k - cost, 0)
        return ans 