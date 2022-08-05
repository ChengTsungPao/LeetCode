class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {}
        def recur(x):
            if x not in memo:
                if x == 1:
                    return 0
                memo[x] = recur(x // 2) + 1 if x % 2 == 0 else recur(3 * x + 1) + 1
            return memo[x]
        
        power_value = []
        for x in range(lo, hi + 1):
            power_value.append((recur(x), x))
        
        # optimal => quick select: O(n)
        return sorted(power_value)[k - 1][1]