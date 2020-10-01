class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        count = 0
        for ch in S:
            if ch in J:
                count += 1
        return count