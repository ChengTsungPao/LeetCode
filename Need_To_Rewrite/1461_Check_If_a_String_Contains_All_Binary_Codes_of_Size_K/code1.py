class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        status = set()
        for i in range(len(s) - k + 1):
            status.add(s[i:i + k])
        return len(status) == 2 ** k