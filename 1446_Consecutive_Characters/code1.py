class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        count = 1
        char = s[0]
        for ch in s[1:]:
            if char != ch:
                ans = max(ans, count)
                char = ch
                count = 1
            else:
                count += 1
        ans = max(ans, count)
        return ans