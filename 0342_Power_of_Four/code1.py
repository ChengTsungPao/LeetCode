class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        Binary = bin(num)
        return num > 0 and Binary.count("1") == 1 and (len(Binary) - Binary.index("1") - 1) % 2 == 0