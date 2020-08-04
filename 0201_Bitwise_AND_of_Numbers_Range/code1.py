class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        import math
        if(m == 0 or int(math.log(n, 2)) - int(math.log(m, 2)) >= 1):
            return 0
        else:
            ans = n
            for i in range(m, n):
                ans &= i
        return ans