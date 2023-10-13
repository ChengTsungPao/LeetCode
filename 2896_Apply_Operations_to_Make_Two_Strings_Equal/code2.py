class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        indices = [idx for idx, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]
        n = len(indices)
        if n % 2:
            return -1
        
        @functools.lru_cache(None)
        def dp(i):
            if i == 0:
                return x / 2
            elif i < 0:
                return 0
            return min(dp(i - 1) + x / 2, dp(i - 2) + indices[i] - indices[i - 1])            
        
        return int(dp(n - 1))