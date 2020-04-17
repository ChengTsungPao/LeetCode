class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        data = list(range(n))
        length = factorial(n)
        s = ""
        for i in range(n,0,-1):
            length //= i
            s += str(data[(k - 1) // length] + 1)
            del data[(k - 1) // length]
            k = k % length
        return s