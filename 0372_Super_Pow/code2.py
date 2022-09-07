class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join([str(d) for d in b])), 1337)