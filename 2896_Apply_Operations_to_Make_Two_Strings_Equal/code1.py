class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        indices = [idx for idx, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]
        n = len(indices)
        if n % 2:
            return -1
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            idx1, idx2, idx3, idx4 = indices[i], indices[i + 1], indices[j - 1], indices[j]
            cost1 = min(x, idx4 - idx1) + dp(i + 1, j - 1)
            cost2 = min(x, idx2 - idx1) + dp(i + 2, j)
            cost3 = min(x, idx4 - idx3) + dp(i, j - 2)
            return min(cost1, cost2, cost3)            
        
        return dp(0, n - 1)